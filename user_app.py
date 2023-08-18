import mysql.connector
import requests
import configparser

currency_list = ['EUR', 'JPY', 'BGN', 'CZK', 'DKK', 'GBP', 'HUF', 'PLN', 'RON', 'SEK', 'CHF', 'ISK', 'NOK', 'TRY', 'AUD', 
                 'BRL', 'CAD', 'CNY', 'HKD', 'IDR', 'INR', 'KRW', 'MXN', 'MYR', 'NZD', 'PHP', 'SGD', 'THB', 'ZAR']


config = configparser.ConfigParser()
config.read("./Ethereum-check/config.ini")

db_host = config.get("database", "host")
db_user = config.get("database", "user")
db_password = config.get("database", "password")
db_database = config.get("database", "database")
db_port = config.get("database", "port")


db_config = {
    "host": db_host,
    "user": db_user,
    "password": db_password,
    "database": db_database,
    "port": db_port
}

# Funkcja do dodawania danych do bazy
def dodaj_dane(name, mail, crypto, currency):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        insert_query = "INSERT INTO user_data (name, mail, crypto, currency) VALUES (%s, %s, %s, %s)"
        data = (name, mail, crypto, currency)

        cursor.execute(insert_query, data)
        connection.commit()

        print("Dane dodane do bazy!")

    except mysql.connector.Error as err:
        print("Błąd podczas dodawania danych:", err)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

try:
    base_url="https://api.coingecko.com/api/v3/coins/list"
    response = requests.get(base_url)
    list_of_crypto=[]
    if response.status_code==200:
        data=response.json()
        for cryptocurrency in data:
            list_of_crypto.append(cryptocurrency["name"].lower())
    name = input("Podaj name: ")
    mail = input("Podaj mail: ")
    crypto=''
    cryptos=''
    while crypto != "koniec" or cryptos=='':
        crypto = input("Podaj crypto (jesli chcesz zakonczyc napisz 'koniec'): ")
        if crypto.lower() in list_of_crypto:
            cryptos+=f" ,{crypto.lower()}"
        elif crypto!="koniec":
            print("Niepoprawna waluta, sprobuj raz jeszcze")
        else:
            pass
    currency=''
    while currency not in currency_list:
        currency = input("Podaj kod waluty w jakiej chcesz widziec kurs: ").upper()

except:
    print("Wystapil blad przy pobieraniu bazy danych z kryptowalutami")

dodaj_dane(name, mail, crypto, currency)