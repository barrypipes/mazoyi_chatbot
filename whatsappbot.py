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
        msg.body('Thank you for your interest in Mazoyi Mixture. How can I help you?\n\nMAIN MENU\n\n1. What is Mazoyi?\n2. Where can I find Mazoyi?\n3. Mazoyi products & prices.\n4. Place your order.\n5. Upload proof of payment\n')
        responded = True

    if 'hi' in incoming_msg:
        # return image of product and greeting
        msg.media('http://pychat.shirlhost.com/images/product.png')
        msg.body('Thank you for your interest in Mazoyi Mixture. How can I help you?\n\nMAIN MENU\n\n1. What is Mazoyi?\n2. Where can I find Mazoyi?\n3. Mazoyi products & prices.\n4. Place your order.\n5. Upload proof of payment\n')
        responded = True

    if 'hello' in incoming_msg:
        # return image of product and greeting
        msg.media('http://pychat.shirlhost.com/images/product.png')
        msg.body('Thank you for your interest in Mazoyi Mixture. How can I help you?\n\nMAIN MENU\n\n1. What is Mazoyi?\n2. Where can I find Mazoyi?\n3. Mazoyi products & prices.\n4. Place your order.\n5. Upload proof of payment\n')
        responded = True
        
    # Menu Trigger Words #
    if 'find' in incoming_msg:
        # retrun location response
        msg.media('http://pychat.shirlhost.com/images/product.png')
        msg.body('If you would like to know where to find Mazoyi Mixture, tell me what province are you in:\n\nCHOOSE YOUR PROVINCE.\n\nA. Eastern Cape\nB. Western Cape\nC. Northern Cape\nD. Northwest\nE.Freestate\nF. Mpumalanga\nG. Gauteng\nH. KwaZulu Natal\nI. Limpopo\n')
        responded = True
        
    if 'where' in incoming_msg:
        # retrun location response
        msg.media('http://pychat.shirlhost.com/images/product.png')
        msg.body('If you would like to know where to find Mazoyi Mixture, tell me what province are you in:\n\nCHOOSE YOUR PROVINCE.\n\nA. Eastern Cape\nB. Western Cape\nC. Northern Cape\nD. Northwest\nE.Freestate\nF. Mpumalanga\nG. Gauteng\nH. KwaZulu Natal\nI. Limpopo\n')
        responded = True

    if 'buy' in incoming_msg:
        # retrun location response
        msg.media('http://pychat.shirlhost.com/images/product.png')
        msg.body('If you would like to know where to find Mazoyi Mixture, tell me what province are you in:\n\nCHOOSE YOUR PROVINCE.\n\nA. Eastern Cape\nB. Western Cape\nC. Northern Cape\nD. Northwest\nE.Freestate\nF. Mpumalanga\nG. Gauteng\nH. KwaZulu Natal\nI. Limpopo\n')
        responded = True
        
    if 'want' in incoming_msg:
        # retrun location response
        msg.media('http://pychat.shirlhost.com/images/product.png')
        msg.body('If you would like to know where to find Mazoyi Mixture, tell me what province are you in:\n\nCHOOSE YOUR PROVINCE.\n\nA. Eastern Cape\nB. Western Cape\nC. Northern Cape\nD. Northwest\nE.Freestate\nF. Mpumalanga\nG. Gauteng\nH. KwaZulu Natal\nI. Limpopo\n')
        responded = True
        
    if 'mazoyi' in incoming_msg:
        # retrun location response
        msg.media('http://pychat.shirlhost.com/images/product.png')
        msg.body('If you would like to know where to find Mazoyi Mixture, tell me what province are you in:\n\nCHOOSE YOUR PROVINCE.\n\nA. Eastern Cape\nB. Western Cape\nC. Northern Cape\nD. Northwest\nE.Freestate\nF. Mpumalanga\nG. Gauteng\nH. KwaZulu Natal\nI. Limpopo\n')
        responded = True
        
    if 'medicine' in incoming_msg:
        # retrun location response
        msg.media('http://pychat.shirlhost.com/images/product.png')
        msg.body('If you would like to know where to find Mazoyi Mixture, tell me what province are you in:\n\nCHOOSE YOUR PROVINCE.\n\nA. Eastern Cape\nB. Western Cape\nC. Northern Cape\nD. Northwest\nE.Freestate\nF. Mpumalanga\nG. Gauteng\nH. KwaZulu Natal\nI. Limpopo\n')
        responded = True
        
    # Provinces #
    if 'eastern cape' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\u25AA East London\n\u25AA Queenstown\n\u25AA King Williams Town\n\u25AA Berlin\n\u25AA Mdantsane\n\u25AA Alice\n\u25AA Fort Beaufort\n\u25AA Mthatha\n\u25AA Idutya\n\u25AA Centane\n\u25AA Butterworth\n\u25AA Engcobo\n\u25AA Ngqamakwe\n\u25AA Tsomo\n\u25AA Elliotdale\n\u25AA Libode\n\u25AA Tsolo\n\u25AA Qumbu\n\u25AA Mount Frere\n\u25AA Mqanduli\n\u25AA PSJ Lusiki\n\u25AA Sterkspruit\n\u25AA Cofimvaba\n') # need to fill this out
        responded = True

    if 'gauteng' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\u25AA Vanderbijlpark') # need to fill this out
        responded = True

    if 'freestate' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\n1. Fickburg\n2. Kroonstad\n3. Welkom\n4. Bethlehem\n5. Parys\n6. Botshabelo\n7. Thaba Nchu\n8. Phuthaditjhaba\n9. Bloemfotein\n10. Odendaalsrus\n11. Virginia Central') # need to fill this out
        responded = True

    if 'western cape' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\n1. Paarl 1\n2. Paarl 2\n3. Kraaifotein 1\n4. Kraaifotein 2\n5. Makhaza\n6. Khayelitsha Site B Mall\n7. Khayelitsha Mall 1\n8. Khayelitsha Mall 2\n9. Site C\n10. Eerste River\n11. Blue Daisy\n12. Michells Plein\n13. Town Centre\n14. Phillippi 2\n14. Phillippi-Plaza\n15. Wynberg\n16. Dorlesville\n17. Kuilsriver\n18. Bellville 1\n19. Bellville 2\n20. Mfuleni') # need to fill this out
        responded = True

    if 'kwazulu natal' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\n1. Durban') # need to fill this out
        responded = True

    if 'limpompo' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\n1. Polokwane') # need to fill this out
        responded = True

    if 'northern cape' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\n1. Hartswater') # need to fill this out
        responded = True

    if 'mpumalanga' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\n1. Nespruit') # need to fill this out
        responded = True

    if 'northwest' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\n1. Potchefstroom\n2. Klerkdorp\n3. Vryburg\n4. Jouberton') # need to fill this out
        responded = True

    if '1' in incoming_msg:
        # return locations in East London
        msg.body('Mazoyi Mixture can be found at these locations:\n\nJohn Forbes Pharmacy, Sounthernwood\nQuigney Pharmacy, Quigney')
        responded = True

    if 'east london' in incoming_msg:
        # return locations in East London
        msg.body('Mazoyi Mixture can be found at these locations:\n\nJohn Forbes Pharmacy, Sounthernwood\nQuigney Pharmacy, Quigney')
        responded = True

    if not responded:
        msg.body('Thank you so much for your interest in Mazoyi Mixture.')
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
