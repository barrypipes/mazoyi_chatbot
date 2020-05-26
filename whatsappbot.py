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
        msg.body('Thank you for your interest in Mazoyi Mixture. How can I help you?\n\nMAIN MENU\n\n\u25AA What is Mazoyi?\n\u25AA Where can I find Mazoyi?\n\u25AA Mazoyi products & prices.\n\u25AA Place your order.\n\u25AA Upload proof of payment\n')
        responded = True

    if 'hi' in incoming_msg:
        # return image of product and greeting
        msg.media('http://pychat.shirlhost.com/images/product.png')
        msg.body('Thank you for your interest in Mazoyi Mixture. How can I help you?\n\nMAIN MENU\n\n\u25AA What is Mazoyi?\n\u25AA Where can I find Mazoyi?\n\u25AA Mazoyi products & prices.\n\u25AA Place your order.\n\u25AA Upload proof of payment\n')
        responded = True

    if 'hello' in incoming_msg:
        # return image of product and greeting
        msg.media('http://pychat.shirlhost.com/images/product.png')
        msg.body('Thank you for your interest in Mazoyi Mixture. How can I help you?\n\nMAIN MENU\n\n\u25AA What is Mazoyi?\n\u25AA Where can I find Mazoyi?\n\u25AA Mazoyi products & prices.\n\u25AA Place your order.\n\u25AA Upload proof of payment\n')
        responded = True

    if 'find' in incoming_msg:
        # retrun location response
        msg.body('If you would like to know where to find Mazoyi Mixture, tell me what province are you in:\n\n\u25AA Gauteng\n\u25AA Freestate\n\u25AA Eastern Cape\n\u25AA Western Cape\n\u25AA KwaZulu Natal\n\u25AA Limpompo\n\u25AA Northwest\n\u25AA Mpumalanga\n\u25AA Northern Cape') # need to fill out provinces
        responded = True

    if 'buy' in incoming_msg:
        # retrun location response
        msg.body('If you would like to know where to find Mazoyi Mixture, tell me what province are you in:\n\n\u25AA Gauteng\n\u25AA Freestate\n\u25AA Eastern Cape\n\u25AA Western Cape\n\u25AA KwaZulu Natal\n\u25AA Limpompo\n\u25AA Northwest\n\u25AA Mpumalanga\n\u25AA Northern Cape') # need to fill out provinces
        responded = True

    if 'eastern cape' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\u25AA East London\n\u25AA Port Elizabeth\n') # need to fill this out
        responded = True

    if 'Gauteng' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\u25AA East London\n\u25AA Port Elizabeth\n') # need to fill this out
        responded = True

    if 'Freestate' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\u25AA East London\n\u25AA Port Elizabeth\n') # need to fill this out
        responded = True

    if 'Western Cape' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\u25AA East London\n\u25AA Port Elizabeth\n') # need to fill this out
        responded = True

    if 'KwaZulu Natal' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\u25AA East London\n\u25AA Port Elizabeth\n') # need to fill this out
        responded = True

    if 'Limpompo' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\u25AA East London\n\u25AA Port Elizabeth\n') # need to fill this out
        responded = True

    if 'Northern Cape' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\u25AA East London\n\u25AA Port Elizabeth\n') # need to fill this out
        responded = True

    if 'Mpumalanga' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\u25AA East London\n\u25AA Port Elizabeth\n') # need to fill this out
        responded = True

    if 'Northwest' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\u25AA East London\n\u25AA Port Elizabeth\n') # need to fill this out
        responded = True

    if '1' in incoming_msg:
        # return locations in East London
        msg.body('Mazoyi Mixture can be found at these locations:\n\n\u25AAJohn Forbes Pharmacy, Sounthernwood\n\u25AAQuigney Pharmacy, Quigney')
        responded = True

    if 'east london' in incoming_msg:
        # return locations in East London
        msg.body('Mazoyi Mixture can be found at these locations:\n\n\u25AAJohn Forbes Pharmacy, Sounthernwood\n\u25AAQuigney Pharmacy, Quigney')
        responded = True

    if not responded:
        msg.body('Thank you so much for your interest in Mazoyi Mixture.')
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
