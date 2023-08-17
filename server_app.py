import requests
import smtplib
from email.mime.text import MIMEText


def get_cryptocurrency_price(crypto_id):
    base_url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "pln",
        "ids": crypto_id,
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        # print(data)
        if data:
            return data[0]["name"], data[0]["symbol"], data[0]["current_price"], data[0]["high_24h"], data[0]["low_24h"], data[0]["price_change_percentage_24h"]
    return None, None, None

def print_cryptocurrency_price():
    crypto_id = "ethereum"  
    name, symbol, price, high, low, percentage_change = get_cryptocurrency_price(crypto_id)

    if name and symbol and price and low and high and percentage_change:
        message=f"{name} ({symbol}): {price:,.2f} PLN\nHigh price (24h): {high:,.2f} PLN\nLow Price (24h): {low:,.2f} PLN\nPrice change (24h): {percentage_change:.2f}%"
    else:
        message="Failed to fetch cryptocurrency data."
    return message

def send_messages():
    message=print_cryptocurrency_price()
    recipients= ['damwid2599@gmail.com', 'damwid@hotmail.com']
    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()
        server.login('cryptocurrency_stock@outlook.com', 'B1TC01N&3th3r3um')

        for recipient in recipients:
            msg = MIMEText(message)
            msg['Subject'] = 'Cryptocurrency change'
            msg['From'] = 'cryptocurrency_stock@outlook.com'
            msg['To'] = recipient

            server.sendmail('cryptocurrency_stock@outlook.com', [recipient], msg.as_string())
    except Exception as e:
        print('Wystapil blad podczas wysylania wiadomosci')
    finally:
        server.quit()

send_messages()


