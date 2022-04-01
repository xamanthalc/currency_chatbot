
#libraries
import json
import requests
from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

#API


##["SGD","MYR","EUR","USD","AUD","JPY","CNH","HKD","CAD","INR","DKK","GBP","RUB","NZD","MXN","IDR","TWD","THB","VND"]
url = "https://currency-exchange.p.rapidapi.com/exchange"

querystring = {"from":"SGD","to":"MYR","q":"1.0"}

headers = {
	"X-RapidAPI-Host": "currency-exchange.p.rapidapi.com",
	"X-RapidAPI-Key": "53fdc976cemsh5e779514bc5e545p1a889bjsnf086b16cbcaf"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


querystring2 = {"from":"USD","to":"EUR","q":"5.0"}

response2 = requests.request("GET", url, headers=headers, params=querystring2)

#chatbox


app = Flask(__name__)


@app.route("/bot", methods=['POST'])



def all():
    incoming_msg = request.form.get('Body')
    response = MessagingResponse()
    message=response.message()
    responded = False
    words = incoming_msg.split(' ')
    
    if "Hello" in incoming_msg:
        reply = "Hi! Let's start. Tell me what currency you want to conver in the format:\n[from origin_currency to final_currency value value_here]\ncurrencies supported: SGD,MYR,EUR,USD,AUD,JPY,CNH,HKD,CAD,INR,DKK,GBP,RUB,NZD,MXN,IDR,TWD,THB,VND"
        message.body(reply)
        print(type(reply))
        responded = True
        
    elif "From" in incoming_msg:
        from_curr = words[1]
        to_curr = words[3]
        value = words[5]
        print(value)
        print(from_curr)
        print(to_curr)
        querystring = {"from": from_curr,"to":to_curr,"q": value}
        repply = requests.request("GET", url, headers=headers, params=querystring)
        repply = repply.text
        repply = float(repply)
        value = float(value)
        repply = repply*value
        repply=str(repply)
        message.body(repply)
        responded = True

    else:
        reply = "Sorry, I did not understand :("
        message.body(reply)
        responded = True
        
    return str(response)




if __name__ == "__main__":
    app.run(debug=True)




    
