import datetime as dt
import smtplib
import keyring
import random

SERVICE = "smtp.gmail.com"
EMAIL = "jason.dynes@googlemail.com"
TEST_EMAIL = "jason.dynes@gmail.com"


def get_quote():
    with open("quotes.txt", "r") as quote_file:
        quotes = quote_file.readlines()
        quote = random.choice(quotes)
        return quote


def send_email():
    quote_to_be_sent = get_quote()
    # google app password created using URL https://myaccount.google.com/apppasswords
    # password stored in windows credential manager as temp setup
    password = keyring.get_password(SERVICE, EMAIL)
    with smtplib.SMTP(SERVICE) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=password)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=TEST_EMAIL,
                            msg=f"Subject: Monday Motivation\n\n"
                                f"{quote_to_be_sent}")


now = dt.datetime.now()
day = now.weekday()
if day == 0:
    send_email()
else:
    pass
