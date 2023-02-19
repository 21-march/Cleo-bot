import datetime
import requests
import json

def request_parse(request: str) -> str:
    return response(request.lower().rstrip("?").split())

def response(parsed_request: list):
    keywords = {
        'date': date(),
        'weather': weather()
    }

    for word in parsed_request:
        if word in keywords:
            return keywords[word]
    return "\nSorry, I cannot seem to fufill this request"

def date() -> str:
    todays_date = str(datetime.datetime.now())
    
    year_month_day = str()
    for i in range(10) : year_month_day += (todays_date[i])

    hour_minutes_seconds = str()
    for i in range(11, 19) : hour_minutes_seconds += (todays_date[i])
    
    return "\nToday's date is: \t" + year_month_day + "\nThe current time is: \t" + hour_minutes_seconds

def weather() -> str:
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    api_key = '48d8b744fa377731a47f6530bf01deee'
    city_request = input("Enter city name: ")
    URL = base_url + "q=" + city_request + "&appid=" + api_key
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()

        main = data['main']
        temperature = round(main['temp'] - 273.15, 3)
        feels_like = round(main['feels_like'] - 273.15, 3)
        humidity = main['humidity']
        report = data['weather'][0]['description']

        return f"{city_request:-^30}\n Temperature: {temperature}\n Feels Like: {feels_like}\n Humidity: {humidity}\n Weather Report: {report}"
    else:
        return "Your request could not be fufilled due to error: " + response.status_code


# should be at the end of this code
# no idea how to fix this
def quit():
    print('Goodbye!')
    return True