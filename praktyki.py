from http.client import responses
import json
import requests
import time
import sqlite3

from datetime import datetime

data = datetime.today()
dzisiaj = data.strftime("%m-%d")
print(dzisiaj)


def pobierzSwieto():
    conn = sqlite3.connect("gediaswieta.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    if not cursor.fetchone():
        print("nie widzę tabeli swietazdrowie")
        conn.close()
        swieto = ""

    else:
        cursor.execute("SELECT Nazwa FROM swietazdrowie WHERE Data=?", (dzisiaj,))
        swieto1 = cursor.fetchone()
        swieto = f", dziś jest także {swieto1[0]}" if swieto1 else ""

    conn.close()

    if swieto:
        return swieto
    return ""


def pobierzImieniny():
    with open("pl.json", "r", encoding="utf-8") as file:
        imieniny = json.load(file)

    dzisiaj = datetime.today().strftime("%d-%m")
    return ", ".join(imieniny[dzisiaj]["nameday"])


def pobierzPogoda():
    apiPogoda_url = "https://api.openweathermap.org/data/2.5/weather?q=nowa%20sol&appid=7b17b7242f3cc13050a78bde816bb0f1&lang=pl"
    response = requests.get(apiPogoda_url)

    if response.status_code == 200:
        dane_pogody = response.json()

        return {
            "temperatura": round(dane_pogody["main"]["temp"] - 273.15),
            "opis": dane_pogody["weather"][0]["description"].capitalize(),
            "odczuwalna": round(dane_pogody["main"]["feels_like"] - 273.15),
            "wilgotnosc": dane_pogody["main"]["humidity"],
            "zachmurzenie": dane_pogody["clouds"]["all"]
        }

    else:
        print("Błąd: Nie udało się pobrać danych pogodowych")
        return {
            "temperatura": "N/A",
            "opis": "Brak danych",
            "odczuwalna": "N/A",
            "wilgotnosc": "N/A"
        }


def generowanieHTML():
    swieto = pobierzSwieto()
    imieniny = pobierzImieniny()
    pogoda = pobierzPogoda()

    try:
        with open("plik.html", "r", encoding="utf-8") as file:
            html = file.read()
    except FileNotFoundError:
        print("Nie widzę pliku `plik.html`!")
        return

    html = html.replace("{{ imieniny }}", imieniny)
    html = html.replace("{{ swieto }}", swieto)
    html = html.replace("{{ temperatura }}", str(pogoda["temperatura"]))
    html = html.replace("{{ opis }}", pogoda["opis"])
    html = html.replace("{{ odczuwalna }}", str(pogoda["odczuwalna"]))
    html = html.replace("{{ wilgotnosc }}", str(pogoda["wilgotnosc"]))
    html = html.replace("{{ zachmurzenie }}", str(pogoda["zachmurzenie"]))

    with open("index.html", "w", encoding="utf-8") as file:
        file.write(html)

    print("Zaktualizowano html")


while True:
    generowanieHTML()
    time.sleep(1800)  # czeka 30 minut, by odświeżyć
