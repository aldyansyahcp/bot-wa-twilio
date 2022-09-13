# bot-wa-twilio
Source from <a href="https://www.twilio.com/blog/build-a-whatsapp-chatbot-with-python-flask-and-twilio">Twilio</a>
<br>Running with flask & ngrok & for automation bot <a href="https://dashboard.herokuapp.com/">Heroku</a>
<br>
```
from os import system
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request

app = Flask(__name__)
@app.route("/bot"):
def ok():
    msg_body = request.values.get("Body","").lower
    msmm = MessagingResponse.message()
    output = False
    if " " in msg_body:
        msmm.body(" Some text to sender wa ")
        output = True

app.run(debug=True, port=3000)
system("ngrok http 3000")
```
want to test my bot? <a href="https://api.whatsapp.com/send/?phone=14155238886&text=join shop-birthday&type=phone_number&app_absent=0">Test me</a>
