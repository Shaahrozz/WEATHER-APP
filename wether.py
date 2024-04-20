import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(city):
    api_key = '58e4e3aecb62907549a2a9f46c65489a'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(url)
        data = response.json()
        if data['cod'] == 200:
            weather = {
                'description': data['weather'][0]['description'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
            return weather
        else:
            return None
    except Exception as e:
        print('Error occurred:', e)
        return None

def get_weather_for_city():
    city = entry_city.get()
    if city:
        weather = get_weather(city)
        if weather:
            messagebox.showinfo('Weather', f"Weather in {city}:\n"
                                            f"Description: {weather['description']}\n"
                                            f"Temperature: {weather['temperature']}°C\n"
                                            f"Humidity: {weather['humidity']}%\n"
                                            f"Wind Speed: {weather['wind_speed']} m/s")
        else:
            messagebox.showerror('Error', f"Failed to fetch weather for {city}")
    else:
        messagebox.showerror('Error', 'Please enter a city')

# Create the main window
root = tk.Tk()
root.title('Weather App')

# Create and place widgets
label_city = tk.Label(root, text='Enter City:')
label_city.grid(row=0, column=0)

entry_city = tk.Entry(root)
entry_city.grid(row=0, column=1)

button_get_weather = tk.Button(root, text='Get Weather', command=get_weather_for_city)
button_get_weather.grid(row=1, column=0, columnspan=2)

# Run the main event loop
root.mainloop()
