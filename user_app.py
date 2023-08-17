import mysql.connector

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

# Pobierz dane od użytkownika
name = input("Podaj name: ")
mail = input("Podaj mail: ")
crypto = input("Podaj crypto (oddzielone przecinkami): ")
currency = input("Podaj walutę: ")

# Wywołaj funkcję do dodawania danych
dodaj_dane(name, mail, crypto, currency)