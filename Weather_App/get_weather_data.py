import requests
import tkinter as tk

def get_weather(city, API_Key):
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200 :
        data =response.json()
        temperature = data['main']['temp']
        weather = data['weather'][0]['description']
        humidity = data['main']['humidity']
        return f'Weather : {weather.capitalize()}\nTemperature:{temperature}\nHumidity:{humidity}'

def show_weather():
    city = city_entry.get()
    API_Key = 'ff1837d75cee1f572857e5b16c1cabcd'
    weather_info = get_weather(city, API_Key)
    result_label.config(text=weather_info)

window = tk.Tk()
window.title("Weather App")

city_label = tk.Label(window, text="enter city name:")
city_label.pack()

city_entry = tk.Entry(window)
city_entry.pack()

get_weather_button = tk.Button(window, text="get weather", command=show_weather)
get_weather_button.pack()

result_label = tk.Label(window, text="", justify=tk.LEFT)
result_label.pack()

window.mainloop()