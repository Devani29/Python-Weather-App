import requests

def weather_app(user_city, user_country_code, user_zip_code, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?zip={user_zip_code},{user_country_code}&q={user_city}&appid={api_key}&units=metric&lang=en'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temperature = round(data['main']['temp'])
        temp_min = round(data['main']['temp_min'])
        temp_max = round(data['main']['temp_max'])

        print(f'''
The weather in {user_city}, {user_country_code} (ZIP Code: {user_zip_code}) is: {weather}, {description}.
Temperature: {temperature}
Temperature minimum: {temp_min}
Temperature maximum: {temp_max}
''')
      
    else:
        print("City Not Found")
    
def main():
    print("Welcome to Banana's weather App")
    user_city = input("Enter your city: ")
    user_country_code = input("Enter your country code (For example Mexico = mx): ")
    user_zip_code = input("Enter your ZIP Code: ")
    api_key = '43cae06a72b79475dd2b698e3748854d'

    weather_app(user_city, user_country_code, user_zip_code, api_key)

main()