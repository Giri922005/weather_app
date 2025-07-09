# weather_app
# Weather App Using API

## 📚 Overview

This is a simple Python-based desktop application that provides real-time weather information for any city using the OpenWeatherMap API. The app uses Tkinter for the graphical user interface (GUI) and the `requests` library to fetch data from the weather API.

## 🎯 Objective

Provide quick and easy access to temperature, weather description, and humidity for a user-specified city.

## 🚀 Features

* GUI-based application using Tkinter
* Fetches real-time weather data from OpenWeatherMap API
* Displays temperature (in Celsius), weather description, and humidity
* Handles invalid city inputs gracefully

## 🛠️ Requirements

* Python 3.x
* `requests` library

You can install the `requests` library using:

```
pip install requests
```

## 🔥 How to Run

1. Clone or download this repository.
2. Get your API key from [OpenWeatherMap](https://openweathermap.org/) by creating a free account.
3. Replace `your_api_key_here` in the Python script with your actual API key.
4. Run the Python script:

```
python weather_app.py
```

## 💻 Usage

* Enter the city name in the input box.
* Click on **Get Weather** button.
* The app will display:

  * Temperature in Celsius
  * Weather description (e.g., cloudy, clear sky)
  * Humidity percentage

## 📦 File Structure

```
weather_app.py       # Main application script
README.md            # Project documentation
```

## 🌱 Future Improvements

* Add weather condition icons
* Improve GUI design with better styling and fonts
* Show more weather details (wind speed, sunrise/sunset)
* Package as an executable (.exe) for easy sharing

## 📜 License

This project is open source and free to use for educational purposes.
