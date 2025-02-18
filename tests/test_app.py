import requests

api_key = '43cae06a72b79475dd2b698e3748854d'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    description = weather_data.json()['weather'][0]['description']
    temp = round(weather_data.json()['main']['temp'])
    temp_min = round(weather_data.json()['main']['temp_min'])
    temp_max = round(weather_data.json()['main']['temp_max'])

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is {temp}°C")
    print(f"The minimum temperature is {temp_min}°C and the maximum temperature is {temp_max}°C")

    print(weather_data.json())