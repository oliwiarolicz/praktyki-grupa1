import requests
import time



def plik_html():

    imieniny="jakies imieniny"
    swieto="jakies swieto"
    pogoda="jakas pogoda"
    odczuwalnaTemperatura="jakas odczuwalna temperatura"
    indexUV="jakis index UV"
    wilgotnoscPowietrza="jakas wilgotnosc powietrza"

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
                    <h1>Dzień dobry, dzisiaj imieniny obchodzą <p id="imieniny">{imieniny}</p>, dziś jest także dzień<p>{swieto}</p></h1> 
                </div>
                <div class="zdj">
                    <img src="tlo_czarne.png">
                </div>
                <div class="godzina">
                    <h1 id="czas"></h1>
                </div>
                <div class="pogoda">
                    <h1>Pogoda</h1>
                    <p id="pogoda">{pogoda}</p>
                </div>
                <div class="wilgotnosc">
                    <h1>Wilgotność powietrza</h1>
                    <p id="wilgotnosc">{wilgotnoscPowietrza}</p>
                </div>
                <div class="uv">
                    <h1>Index UV</h1>
                    <p>{indexUV}</p>
                </div>
                <div class="odczuwalna">
                    <h1>Odczuwalna temperatura</h1>
                    <p id="odczuwalna">{odczuwalnaTemperatura}</p>
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


