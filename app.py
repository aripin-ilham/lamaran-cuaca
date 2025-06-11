from flask import Flask, render_template, request
import requests, os, folium
from geopy.geocoders import Nominatim

app = Flask(__name__)
API_KEY = os.getenv("API_KEY", "Your_Api_key")
BASE_CURR = "http://api.openweathermap.org/data/2.5/weather"
BASE_FORE = "http://api.openweathermap.org/data/2.5/forecast"

def geocode(city):
    geolocator = Nominatim(user_agent="weather_app")
    loc = geolocator.geocode(city)
    return (loc.latitude, loc.longitude) if loc else (None, None)

def get_weather(city):
    r = requests.get(BASE_CURR, params={"q": city, "appid": API_KEY, "units": "metric"})
    data = r.json()
    if r.status_code != 200:
        return {"error": data.get("message","Error").capitalize()}
    return {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "desc": data["weather"][0]["description"].capitalize(),
        "humidity": data["main"]["humidity"],
        "wind": data["wind"]["speed"],
    }

def get_forecast(city):
    r = requests.get(BASE_FORE, params={"q": city, "appid": API_KEY, "units": "metric"})
    j = r.json()
    if j.get("cod") != "200":
        return {"error": j.get("message","Error").capitalize()}
    return [
        {"dt": item["dt_txt"].split()[0],
         "temp": item["main"]["temp"],
         "icon": item["weather"][0]["icon"]}
        for item in j["list"] if "12:00:00" in item["dt_txt"]
    ]

@app.route("/", methods=["GET","POST"])
def index():
    weather = None; forecast = None; map_html = None
    if request.method == "POST":
        city = request.form["city"].strip()
        weather = get_weather(city)
        if not weather.get("error"):
            forecast = get_forecast(city)
            lat, lon = geocode(city)
            if lat and lon:
                m = folium.Map(location=[lat, lon], zoom_start=10)
                folium.Marker([lat, lon], tooltip=city).add_to(m)
                map_html = m._repr_html_()
    return render_template("index.html", weather=weather, forecast=forecast, map_html=map_html)

if __name__=="__main__":
    app.run(debug=True)
