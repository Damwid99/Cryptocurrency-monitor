import mysql.connector
import requests


# Konfiguracja połączenia z bazą danych
db_config = {
    "host": "sql7.freesqldatabase.com",
    "user": "sql7640486",
    "password": "l2zDVEwXgI",
    "database": "sql7640486",
    "port": 3306
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
    print(list_of_crypto)
    name = input("Podaj name: ")
    mail = input("Podaj mail: ")
    crypto=''
    cryptos=''
    while crypto != "koniec" and cryptos=='':
        crypto = input("Podaj crypto (jesli chcesz zakonczyc napisz 'koniec'): ")
        if crypto.lower() in list_of_crypto:
            cryptos+=f" ,{crypto.lower()}"
        else:
            print("Niepoprawna waluta, sprobuj raz jeszcze")
    currency = input("Podaj walutę w jakiej chcesz widziec kurs: ")

except:
    print("Wystapil blad przy pobieraniu bazy danych z kryptowalutami")



# Wywołaj funkcję do dodawania danych
#dodaj_dane(name, mail, crypto, currency)