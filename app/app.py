from flask import Flask, request, render_template
import requests, json, os
from bs4 import BeautifulSoup as bs
from twilio.twiml.messaging_response import MessagingResponse
from time import sleep

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    return "<center><b><h1>STATUS ONLINED</b></h1></center>"

@app.route("/bot", methods=["POST", "GET"])
def messageBot():
    msg_body = request.values.get("Body", "").lower()
    print(msg_body)
    res = MessagingResponse()
    respm = res.message()
    hasil = False
    if "coba" in msg_body:
        url = "https://otakudesu.watch/wp-content/uploads/2020/10/Dragon-Quest-Sub-Indo.jpg"
        respm.media(url)
        hasil=True
        
    if "start" in msg_body:
        tek = "Hello bitch welcome tu mobilejen "
        respm.body(tek)
        hasil = True
        
    if "lo ngentod juga" in msg_body:
        tek = "*YATIM LU BANGSAT GW PUKUL JUGA LU PEDO*"
        respm.body(tek)
        hasil=True
                
    if "/help" in msg_body:
        respm.body("LO NGENTOD")
        hasil=True

    if "/rek" in msg_body:
        inp = msg_body[4:]
        r = requests.get("https://otakudesu.watch/anime-list").text
        b = bs(r, "html.parser"); nm=[]
        [nm.append(i.get_text()) for i in b.find_all("a", "hodebgst")]
        [respm.body(i, end="\n\n") for i in nm[0:50]]
        hasil=True
        
    if hasil == False:
        respm.body("gataw ajg")
    return str(res)

if __name__ == "__main__":
    app.run(port=3000, debug=True)
