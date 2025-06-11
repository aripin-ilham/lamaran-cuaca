# 🌤️ SoftUI Weather App

Aplikasi web untuk melihat cuaca saat ini, forecast 5 hari, serta peta lokasi kota.  
Dibuat dengan **Flask**, **OpenWeatherMap API**, **Bootstrap Soft‑UI**, **Folium**, dan **Geopy**.

---

## 🚀 Fitur

- 🔍 Cuaca real-time (suhu, kelembapan, deskripsi, angin)  
- 📅 Forecast 5 hari dalam layout responsif  
- 🗺️ Peta kota interaktif  
- 🌙 Mode gelap dengan toggle sederhana

---

## 🛠️ Instalasi

```bash
git clone https://github.com/USERNAME/softui-weather.git
cd softui-weather
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

export OPENWEATHER_API_KEY="YOUR_API_KEY"  # Linux/Mac
set OPENWEATHER_API_KEY="YOUR_API_KEY"     # Windows

python app.py
