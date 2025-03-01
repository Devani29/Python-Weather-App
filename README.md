# 🌤️ Banana's Weather App

A simple weather application built with Python and Tkinter that fetches real-time weather data using an API.

## 📌 Features
- 🌎 Get weather updates by **city name** or **ZIP code**.
- 🌦️ Displays **temperature, humidity, wind speed, and pressure**.
- 💻 User-friendly graphical interface with Tkinter.
- 🕓 Shows **local time** of the selected location.

## 🔧 Installation

### 1️⃣ Clone the Repository
git clone https://github.com/Devani29/Python-Weather-App.git
cd Python-WeatherApp

### 2️⃣ Install Dependencies
Make sure you have Python 3 installed. Then, set up a virtual environment and install dependencies:

py -m venv venv
source venv/bin/activate                # On macOS/Linux
venv\Scripts\activate                   # On Windows

pip install -r requirements.txt

### 3️⃣ Run the Application
py src/main.py

## 📝 Project Structure
Python-WeatherApp/
|── src/
|   |── assets/
|   |   |── images/                             # Icons and images
|   |── config/
        |── environment_variable.py
|   |── data/
        |── .gitignore
        |── requirements.txt
|   |── modules/
        |── button_events.py                    # Button interactions
        |── focus_events.py                     # Event handlers for text fields
        |── labels_elements.py                  # Info labels
        |── ui_elements.py                      # UI components
        |── weather_app.py                      # Main application logic
        |── weather_service.py                  # API integration
|   |── utils/
|   |     |── log/
|   |         |── logging_config.py             # Logging configuration    
|   |── main.py                                 # Entry point of the app
|── README.md

## 🖥️ Technologies Used
🔹Python 🐍
🔹Tkinter 🎨
🔹Requests 🌐
🔹Logging 📥
🔹PIL 🖼️

## 📃 License
This project is licensed under the MIT License - see the LICENSE file for details.