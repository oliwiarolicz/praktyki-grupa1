setTimeout("location.reload()",1000*60);//czeka minute by odswierzyc


                let czas=new Date();
                let godzina=czas.getHours();
                let minuty=czas.getMinutes();
                if (minuty < 10) minuty = "0" + minuty;
                document.getElementById("czas").innerHTML=godzina+":"+minuty;