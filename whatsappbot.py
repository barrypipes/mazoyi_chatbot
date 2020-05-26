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
        msg.body('If you would like to know where to find Mazoyi Mixture, tell me what province are you in:\n\nGauteng\nFreestate\nEastern Cape\nWestern Cape\nKwaZulu Natal\nLimpompo\nNorthwest\nMpumalanga\nNorthern Cape') # need to fill out provinces
        responded = True

    if 'buy' in incoming_msg:
        # retrun location response
        msg.body('If you would like to know where to find Mazoyi Mixture, tell me what province are you in:\nGauteng\nFreestate\nEastern Cape\nWestern Cape\nKwaZulu Natal\nLimpompo\nNorthwest\nMpumalanga\nNorthern Cape') # need to fill out provinces
        responded = True
        
        # Provinces #
    if 'Eastern Cape' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\n1. East London\n2. Queenstown\n3. King Williams Town\n4. Berlin\n5. Mdantsane\n6. Alice\n7. Fort Beaufort\n8. Mthatha\n9. Idutya\n10. Centane\n11. Butterworth\n12. Engcobo\n13. Ngqamakwe\n14. Tsomo\n14. Elliotdale\n15. Libode\n16. Tsolo\n17. Qumbu\n18. Mount Frere\n19. Mqanduli\n20. PSJ Lusiki\n21. Sterkspruit') # need to fill this out
        responded = True

    if 'Gauteng' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\n1. Vanderbijlpark') # need to fill this out
        responded = True

    if 'Freestate' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\n1. Fickburg\n2. Kroonstad\n3. Welkom\n4. Bethlehem\n5. Parys\n6. Botshabelo\n7. Thaba Nchu\n8. Phuthaditjhaba\n9. Bloemfotein\n10. Odendaalsrus\n11. Virginia Central') # need to fill this out
        responded = True

    if 'Western Cape' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\n1. Paarl 1\n2. Paarl 2\n3. Kraaifotein 1\n4. Kraaifotein 2\n5. Makhaza\n6. Khayelitsha Site B Mall\n7. Khayelitsha Mall 1\n8. Khayelitsha Mall 2\n9. Site C\n10. Eerste River\n11. Blue Daisy\n12. Michells Plein\n13. Town Centre\n14. Phillippi 2\n14. Phillippi-Plaza\n15. Wynberg\n16. Dorlesville\n17. Kuilsriver\n18. Bellville 1\n19. Bellville 2\n20. Mfuleni') # need to fill this out
        responded = True

    if 'KwaZulu Natal' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\n1. East London\n2. Port Elizabeth\n') # need to fill this out
        responded = True

    if 'Limpompo' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\n1. East London\n2. Port Elizabeth\n') # need to fill this out
        responded = True

    if 'Northern Cape' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\n1. East London\n2. Port Elizabeth\n') # need to fill this out
        responded = True

    if 'Mpumalanga' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\n1. East London\n2. Port Elizabeth\n') # need to fill this out
        responded = True

    if 'Northwest' in incoming_msg:
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
