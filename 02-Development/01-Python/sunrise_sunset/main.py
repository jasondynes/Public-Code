import requests
from datetime import datetime

MY_LAT = 51.507351
MY_LONG = -0.127758
URL = "https://api.sunrise-sunset.org/json"
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
sunset_hour = int(sunset.split("T")[1].split(":")[0])
current_hour = int(datetime.now().hour)

if current_hour > sunset_hour:
    print("It is dark outside.")
else:
    print("It is light outside.")