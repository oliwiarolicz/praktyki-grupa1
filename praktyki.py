from http.client import responses

import requests
import time
import sqlite3

from datetime import datetime



data = datetime.today()
dzisiaj = data.strftime("%m-%d")
print(dzisiaj)






conn = sqlite3.connect("gediaswieta.db")
cursor = conn.cursor()


cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
if not cursor.fetchone():
    print("nie widze tabeli swietazdrowie")
    swieto = "brak swieta na dzis"
else:
    cursor.execute("SELECT Nazwa FROM swietazdrowie WHERE Data=?", (dzisiaj,))
    swieto=cursor.fetchone()

if not swieto:
        swieto = "brak swieta na dzis"
#swieto = cursor.fetchall()








apiPogoda_url = "https://api.openweathermap.org/data/2.5/weather?q=nowa%20sol&appid=7b17b7242f3cc13050a78bde816bb0f1&lang=pl"
response = requests.get(apiPogoda_url)

def plik_html():
    if response.status_code == 200:
        dane_pogody = response.json()

        temperatura = dane_pogody["main"]["temp"] - 273.15
        opis = dane_pogody["weather"][0]["description"]
        odczuwalna = dane_pogody["main"]["feels_like"] - 273.15
        wilgotnosc = dane_pogody["main"]["humidity"]

        print(f"Pogoda: {round(temperatura)}°C, {opis.capitalize()}")
        print(f"Odczuwalna temperatura: {round(odczuwalna)}°C")
        print(f"Wilgotność: {wilgotnosc}%")
    else:
        print("Błąd: Nie udało się pobrać danych pogodowych")


    conn.close()
    #swieto="jakies swieto"
    #temperatura="jakas pogoda"
    #odczuwalnaTemperatura="jakas odczuwalna temperatura"
    indexUV="jakis index UV"
    #wilgotnosc="jakas wilgotnosc powietrza"
    imieniny="jakies imieniny"
    #opis="jakis opis"

    htmlcontent = f"""<!DOCTYPE html>
    <html lang="pl">
        <head>
            <meta charset="utf-8">
            <title>Pogoda Gedia</title>
            <link rel="stylesheet" href="styl.css">
        </head>
        <body>
            <div class="strona">
                <div class="puste1">
                    <h1></h1> 
                </div>
                <div class="puste2">
                    <h1></h1> 
                </div>
                <div class="puste3">
                    <h1></h1> 
                </div>
                <div class="dzien">
                    <h1>Dzień dobry,<br> dzisiaj imieniny obchodzą {imieniny}, dziś jest także {swieto}</h1> 
                </div>
                <div class="zdj">
                    <img src="tlo_czarne.png">
                </div>
                <div class="godzina">
                    <h1 id="czas"></h1>
                </div>
                <div class="pogoda">
                    <h1>Pogoda</h1>
                    <p id="pogoda">{round(temperatura)}°C, {opis}</p>
                </div>
                <div class="wilgotnosc">
                    <h1>Wilgotność powietrza</h1>
                    <p id="wilgotnosc">{wilgotnosc}%</p>
                </div>
                <div class="uv">
                    <h1>Index UV</h1>
                    <p>{indexUV}</p>
                </div>
                <div class="odczuwalna">
                    <h1>Odczuwalna temperatura</h1>
                    <p id="odczuwalna">{round(odczuwalna)}°C</p>
                </div>
            </div>
            
            
            <script>
                 setTimeout("location.reload()",1000*60);//czeka minute by odswierzyc


                let czas=new Date();
                let godzina=czas.getHours();
                let minuty=czas.getMinutes();
                let sekundy=czas.getSeconds();
                document.getElementById("czas").innerHTML=godzina+":"+minuty;
            </script>
        </body>
    </html>"""


    with open("plik.html", "w", encoding="utf-8") as file:
        file.write(htmlcontent)



while True:
    plik_html()
    time.sleep(1800)  #czeka 30 min by odswierzyc


