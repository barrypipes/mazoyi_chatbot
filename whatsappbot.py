from flask import Flask, redirect, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)



@app.route('/')
def index():
    return "ChatBot waiting..."


@app.route('/bot', methods=["POST", "GET"])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    
    # Greetings #
    if 'molo' in incoming_msg:
        # return image of product and greeting
        msg.media('http://pychat.shirlhost.com/images/product.png')
        msg.body('Thank you for your interest in Mazoyi Mixture http://www.mazoyigroup.co.za. How can I help you?')
        responded = True
    if 'hi' in incoming_msg:
        # return image of product and greeting
        msg.media('http://pychat.shirlhost.com/images/product.png')
        msg.body('Thank you for your interest in Mazoyi Mixture http://www.mazoyigroup.co.za. How can I help you?')
        responded = True
    if 'hello' in incoming_msg:
        # return image of product and greeting
        msg.media('http://pychat.shirlhost.com/images/product.png')
        msg.body('Thank you for your interest in Mazoyi Mixture http://www.mazoyigroup.co.za. How can I help you?')
        responded = True
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    if 'find' in 
    return str(resp)
    

if __name__ == "__main__":
    app.run(debug=True)