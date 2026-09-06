import requests
import smtplib
from dotenv import load_dotenv
import os



smtp = 'smtp.gmail.com'
sender = 'emil@example.com'
password = '1234556'
receiver = 'tobias@example.com'
message = 'Subject: Rain Alert\n\nIt is going to Rain to day, Bring an ☂️'



API = "http://api.openweathermap.org/data/2.5/forecast"
load_dotenv()
API_KEY = os.getenv('API_KEY')

WEATHER_PARAMS = {
    "lat": 25.2988889,
    "lon": 91.5813889,

    "appid": API_KEY,
    "units": "metric",
    "lang": "en",
    "cnt": 4,
}


response = requests.get(url=API, params=WEATHER_PARAMS)
response.raise_for_status()


weather_data = response.json()


# check the weather if the days code is lower then 700 it means it is time to bring an umbrella


def check_for_rain():
    will_rain = False
    print(f"--------------Weather Report--------------")
    print(f"{weather_data['city']['country']} - {weather_data['city']['name']}")

    for i, day in enumerate(weather_data["list"], start=1):
        d = day["weather"][0]
        weather_id = d["id"]
        time = day['dt_txt']

        print(f"--------------{i}.{time}--------------")
        print(f"{d['main']}: {d['description']}")

        if weather_id < 700:
            will_rain = True
            print("Bring an Umbrella with you")

    if will_rain:
        print(message)
        # try:
        #     with smtplib.SMTP(smtp) as connection:
        #         connection.starttls()
        #         connection.login(sender,password)
        #         connection.sendmail(from_addr=sender,to_addrs=receiver,msg=message)
        # except Exception as e:
        #     print(e)
    else:
        print('no rain')


def main():
    check_for_rain()

if __name__ == "__main__":
    main()