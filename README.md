💰 BITCOIN BUY THE DIP AUTOMATION 🤑

A python script to make multiple bitcoin buy requests at various percentages of current price to leverage bitcoin volatility.

✨ Technologies

    Python
    AWS Lambda
    AWS Secrets Manager
    Bitaroo

🚀 Features

    Customisable purchase amount
    Includes lambda file if you want to host it on lambda like me
    Customisable purchase frequency
    Customisable batch size

📍 The Process

I started buying bitcoin weekly once it started to crash (call it optimism) and wanted to automate the process. I found that automising the actual purchasing was pretty easy and then saw that I could make specific purchase orders for when bitcoin hit a certain price. Upon realising all the possible savings I was possibly missing out on by buying at the same time every week I decided I could make something better. After a little thinking I settled on the simple multi purchase order system. I put in a request to buy it at 98%, 95% and 92% of its current price. If it hits those prices boom: Huge Savings. Otherwise the buys go through when the code runs again, no harm no foul. At the end of the day you're still buying X amount a week. Just now you have an edge and with something as volatile as btc you're super likely to be getting the best prices of the week.

🚦 Running the Project

    Clone the repository
    Fill out the variable fields with your own API keys and purchase amount
    Run the file yourself / Automate it somehow / Put it on AWS Lambda
