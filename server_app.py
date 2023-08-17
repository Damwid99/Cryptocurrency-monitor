import requests
import smtplib
import mysql.connector
from email.mime.text import MIMEText
from forex_python.converter import CurrencyRates


# Konfiguracja połączenia z bazą danych
db_config = {
    "host": "sql7.freesqldatabase.com",
    "user": "sql7640486",
    "password": "l2zDVEwXgI",
    "database": "sql7640486",
    "port": 3306
}


class Client:
    def __init__(self, name, mail, cryptos, currency):
        self.name = name
        self.mail = mail
        self.cryptos = [crypto.strip() for crypto in cryptos.split(',')]
        self.currency = currency

        self.message=f"Hello {self.name},\n\n"
    
    def create_message(self, crypto_name, crypto_symbol, crypto_price, high, low, percentage_change):
        c=CurrencyRates()
        crypto_price=c.convert('USD',self.currency, crypto_price)
        high=c.convert('USD',self.currency, high)
        low=c.convert('USD',self.currency, low)
        self.message+=f"{crypto_name} ({crypto_symbol}): {crypto_price:,.2f} {self.currency}\nHigh price (24h): {high:,.2f} {self.currency}\nLow Price (24h): {low:,.2f} {self.currency}\nPrice change (24h): {percentage_change:.2f}%\n\n"


def get_clients_from_database():
    list_of_clients=[]
    try:
        connection = mysql.connector.connect(**db_config)
        cursor=connection.cursor()

        select_query="SELECT name, mail, crypto, currency FROM user_data"
        cursor.execute(select_query)

        data = cursor.fetchall()
        for row in data:
            name, mail, crypto, currency = row
            list_of_clients.append(Client(name, mail, crypto, currency))
    except mysql.connector.Error as err:
        print("Wystapil blad podczas pobierania danych: ", err)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    return list_of_clients


def send_messages(clients):
    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()
        server.login('cryptocurrency_stock@outlook.com', 'B1TC01N&3th3r3um')

        for client in clients:
            msg = MIMEText(client.message)
            msg['Subject'] = 'Cryptocurrency change'
            msg['From'] = 'cryptocurrency_stock@outlook.com'
            msg['To'] = client.mail

            server.sendmail('cryptocurrency_stock@outlook.com', [client.mail], msg.as_string())
    except Exception as e:
        print('Wystapil blad podczas wysylania wiadomosci')
    finally:
        server.quit()

def get_prize_for_cryptos(clients):
    list_of_cryptos_to_check_prize=[]
    for client in clients:
        list_of_cryptos_to_check_prize.extend(client.cryptos)
    list_of_cryptos_to_check_prize=list(dict.fromkeys(list_of_cryptos_to_check_prize))
    for cryptocurrency in list_of_cryptos_to_check_prize:
        base_url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "ids": cryptocurrency,
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data:
                for client in clients:
                    if cryptocurrency in client.cryptos:
                        client.create_message(data[0]["name"], data[0]["symbol"], data[0]["current_price"], data[0]["high_24h"], data[0]["low_24h"], data[0]["price_change_percentage_24h"]) 
        #get crypto exchange rate

clients=get_clients_from_database()
get_prize_for_cryptos(clients)

for client in clients:
    print(client.message)

send_messages(clients)


