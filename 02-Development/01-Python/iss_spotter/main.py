import time
import requests
from datetime import datetime
import smtplib
import keyring

# used https://www.latlong.net/ to get lats and longs
MY_LAT = 51.948360  # Your latitude
MY_LONG = -0.282240  # Your longitude
# email service
SERVICE = "smtp.gmail.com"
EMAIL = "jason.dynes@googlemail.com"
TEST_EMAIL = "jason.dynes@gmail.com"


def iss_visible():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now <= sunrise or time_now >= sunset:
        return True
    else:
        return False


def send_email():
    # google app password created using URL https://myaccount.google.com/apppasswords
    # password stored in windows credential manager as temp setup
    password = keyring.get_password(SERVICE, EMAIL)
    with smtplib.SMTP(SERVICE) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=password)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=TEST_EMAIL,
                            msg="Subject: ISS Visible\n\nThe ISS is now visible in the sky!")


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if iss_visible() and is_night():
        send_email()

