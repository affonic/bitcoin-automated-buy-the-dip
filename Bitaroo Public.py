import requests


#User Input:
Trade_Amount = XXXX # <- Replace XXXX with how much you'd like each buy in to be.
Bearer_Token = XXXX # <- Replace XXXX with API Key in form KeyID.secret

#Trade_Amount should be set to a quarter of how much you'd like to invest
#everytime the script is run. I invest 200 a week so i set it to 50.


#Api's:
balance_api = "https://api.bitaroo.com.au/v1/balances"
order_api = "https://api.bitaroo.com.au/v1/orders"
order_book_api = "https://api.bitaroo.com.au/v1/market/order-book"

#Authorization:
headers = {
    "Authorization": f"Bearer {Bearer_Token}"
}

def check_aud_balance():

    balance_response = requests.get(balance_api, headers=headers)

    balance_data = balance_response.json()

    for data in balance_data:
        if data["assetSymbol"] == "aud":
            balance = data["avaliable"]
    
    return balance

def delete_open_orders():
    try:
        order_response  = requests.get(order_api, headers=headers)
    except requests.exceptions.RequestException as e:
        print("API Get Open Orders Error")
        raise SystemExit(e)
    
    order_data = order_response.json()
    
    deleted_order_count = 0

    for order in order_data:
        if order["status"] == "open":
            try:
                order_id = order["orderId"]
                delete_response = requests.delete(f"https://api.bitaroo.com.au/v1/orders/{order_id}", headers=headers)
                delete_data = delete_response.json()
                if delete_data["success"] == "true":
                    deleted_order_count += 1
            except requests.exceptions.RequestException as e:
                print("API Deleting Order Error")
                raise SystemExit(e)
    
    return deleted_order_count
            
def get_price():
    try:
        order_book_response = requests.get(order_book_api)
    except requests.exceptions.RequestException as e:
        print("API Get Price Error")
        raise SystemExit(e)

    order_book_data = order_book_response.json()

    return order_book_data["sell"][0]["price"]

def place_order(price):

    payload = {
      "orderType": "limit",
      "side": "buy",
      "price": price,
      "amount": f"{Trade_Amount/price:.6f}",
      "hidden": False,
      "tif": "gtc"
    }
    try:
        make_order_response = requests.post(order_api, headers=headers, json=payload)
        order_data = make_order_response.json()
        print(order_data)
        return order_data["orderId"]
    except requests.exceptions.RequestException as e:
        print("API Place Order Error")
        raise SystemExit(e)
    
def place_old_orders_quick(price, old_orders):
    price = float(price)
    order_prices = [price] * old_orders 

    order_numbers = []
    
    for prices in order_prices:
        order_numbers.append(place_order(prices))

    return order_numbers

def place_all_orders(price):
    price = float(price)
    order_prices = [price, price*0.98, price*0.95, price*0.93]

    order_numbers = []
    
    for prices in order_prices:
        order_numbers.append(place_order(prices))

    return order_numbers

def main():
    
    price = get_price()

    #Quick Buying Old Orders
    deleted_orders = delete_open_orders()
    if deleted_orders > 0:
        place_old_orders_quick(price, deleted_orders) 
    
    #Making New Orders
    if check_aud_balance() >= 200:
        order_numbers = place_all_orders(price)



if __name__ == "__main__":
    main()
