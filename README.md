# Aplikacja do śledzenia Kryptowalut

## Opis

Te dwie aplikacje zostały stworzone do śledzenia cen kryptowalut i umożliwiają użytkownikom rejestrowanie się w systemie oraz wybieranie interesujących ich kryptowalut do śledzenia.

## Instalacja

1. Sklonuj to repozytorium:

```bash
https://github.com/Damwid99/Ethereum-check.git
`````
2. Zainstaluj wymagane biblioteki za pomocą pliku requirements.txt:
```bash
pip install -r requirements.txt
`````
## Konfiguracja
Uzupełnij plik config.ini zgodnie z przykładem config.example.ini.

config.example.ini:
```bash
[database]
host = sqldatabase.com
user = sql11111
password = your_password
database = sq111111
port = 1111

[email]
smtp_server = smtp.your_mail_server.com
smtp_port = 111
sender_email = your@mail.com
sender_password = your_mail_password
`````

## Użycie
### Aplikacja server_app.py
Uruchom aplikację do wysyłania wiadomości:
```bash
python server_app.py
`````
### Aplikacja user_app.py
Uruchom aplikację do rejestracji użytkowników:
```bash
python user_app.py
`````
## Autor
Damwid99
