import tkinter as tk
from PIL import Image, ImageTk
import requests
from tkinter import font

key = "bb1526772749b4035481924f4a8c1172"


HEIGHT = 700
WIDTH = 700
root = tk.Tk()
root.geometry("700x800")

## formatting response
def format_response(weather):
    try:
        name = weather["name"]
        desc = weather["weather"][0]["description"]
        temp = weather["main"]["temp"]

        final_str = "City: %s \nConditions: %s \nTemperature (C): %s" % (
            name,
            desc,
            temp,
        )
    except:
        final_str = ""

    return final_str


## weather extract from API
def get_weather(city):
    weather_key = "bb1526772749b4035481924f4a8c1172"
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {"appid": weather_key, "q": city, "units": "Metric"}

    response = requests.get(url, params=params)
    weather = response.json()

    label["text"] = format_response(weather)


## background image
bg_img = Image.open(
    "C:\\Users\\SAMSUNG\\Desktop\\enochk\\Python Programs\\Tkinter_weather_GUI\\totoro.jpg"
)
# bg_img = bg_img.resize((HEIGHT, WIDTH), Image.ANTIALIAS)
bg_img = ImageTk.PhotoImage(bg_img)
bg_label = tk.Label(root, image=bg_img)
bg_label.pack()

## container
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

## frame
frame = tk.Frame(root, bg="purple", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

## search bar
entry = tk.Entry(frame, font=("arial", 20))
entry.place(relwidth=0.65, relheight=1)

## search button
button = tk.Button(
    frame, text="Search", font=("arial", 20), command=lambda: get_weather(entry.get())
)
button.place(relx=0.7, relwidth=0.3, relheight=1)

## frame for lower space
lower_frame = tk.Frame(root, bg="purple", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(lower_frame, text="Label", bg="white", font=("Arial", 30))
label.place(relwidth=1, relheight=1)

root.mainloop()
