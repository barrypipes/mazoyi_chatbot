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
        msg.body('Thank you for your interest in Mazoyi Mixture. How can I help you?\n\nMAIN MENU\n\n1. What is Mazoyi?\n2. Where can I find Mazoyi?\n3. Mazoyi products & prices.\n4. Place your order.\n5. Upload your reference number\n')
        responded = True

    if 'hi' in incoming_msg:
        # return image of product and greeting
        msg.media('http://pychat.shirlhost.com/images/product.png')
        msg.body('Thank you for your interest in Mazoyi Mixture. How can I help you?\n\nMAIN MENU\n\n1. What is Mazoyi?\n2. Where can I find Mazoyi?\n3. Mazoyi products & prices.\n4. Place your order.\n5. Upload your reference number\n')
        responded = True

    if 'hello' in incoming_msg:
        # return image of product and greeting
        msg.media('http://pychat.shirlhost.com/images/product.png')
        msg.body('Thank you for your interest in Mazoyi Mixture. How can I help you?\n\nMAIN MENU\n\n1. What is Mazoyi?\n2. Where can I find Mazoyi?\n3. Mazoyi products & prices.\n4. Place your order.\n5. Upload your reference number\n')
        responded = True
        
    if 'hey' in incoming_msg:
        # return image of product and greeting
        msg.media('http://pychat.shirlhost.com/images/product.png')
        msg.body('Thank you for your interest in Mazoyi Mixture. How can I help you?\n\nMAIN MENU\n\n1. What is Mazoyi?\n2. Where can I find Mazoyi?\n3. Mazoyi products & prices.\n4. Place your order.\n5. Upload your reference number\n')
        responded = True
        
    # Menu Trigger Words #
    if 'find' in incoming_msg:
        # return image of product and greeting
        msg.media('http://pychat.shirlhost.com/images/product.png')
        msg.body('Thank you for your interest in Mazoyi Mixture. How can I help you?\n\nMAIN MENU\n\n1. What is Mazoyi?\n2. Where can I find Mazoyi?\n3. Mazoyi products & prices.\n4. Place your order.\n5. Upload your reference number\n')
        responded = True
        
    if 'where' in incoming_msg:
        # return image of product and greeting
        msg.media('http://pychat.shirlhost.com/images/product.png')
        msg.body('Thank you for your interest in Mazoyi Mixture. How can I help you?\n\nMAIN MENU\n\n1. What is Mazoyi?\n2. Where can I find Mazoyi?\n3. Mazoyi products & prices.\n4. Place your order.\n5. Upload your reference number\n')
        responded = True

    if 'buy' in incoming_msg:
        # return image of product and greeting
        msg.media('http://pychat.shirlhost.com/images/product.png')
        msg.body('Thank you for your interest in Mazoyi Mixture. How can I help you?\n\nMAIN MENU\n\n1. What is Mazoyi?\n2. Where can I find Mazoyi?\n3. Mazoyi products & prices.\n4. Place your order.\n5. Upload your reference number\n')
        responded = True
        
    if 'want' in incoming_msg:
        # return image of product and greeting
        msg.media('http://pychat.shirlhost.com/images/product.png')
        msg.body('Thank you for your interest in Mazoyi Mixture. How can I help you?\n\nMAIN MENU\n\n1. What is Mazoyi?\n2. Where can I find Mazoyi?\n3. Mazoyi products & prices.\n4. Place your order.\n5. Upload your reference number\n')
        responded = True
        
    if 'mazoyi' in incoming_msg:
        # return image of product and greeting
        msg.media('http://pychat.shirlhost.com/images/product.png')
        msg.body('Thank you for your interest in Mazoyi Mixture. How can I help you?\n\nMAIN MENU\n\n1. What is Mazoyi?\n2. Where can I find Mazoyi?\n3. Mazoyi products & prices.\n4. Place your order.\n5. Upload your reference number\n')
        responded = True
        
    if 'medicine' in incoming_msg:
       # return image of product and greeting
        msg.media('http://pychat.shirlhost.com/images/product.png')
        msg.body('Thank you for your interest in Mazoyi Mixture. How can I help you?\n\nMAIN MENU\n\n1. What is Mazoyi?\n2. Where can I find Mazoyi?\n3. Mazoyi products & prices.\n4. Place your order.\n5. Upload your reference number\n')
        responded = True
        
    if 'get' in incoming_msg:
        # return image of product and greeting
        msg.media('http://pychat.shirlhost.com/images/product.png')
        msg.body('Thank you for your interest in Mazoyi Mixture. How can I help you?\n\nMAIN MENU\n\n1. What is Mazoyi?\n2. Where can I find Mazoyi?\n3. Mazoyi products & prices.\n4. Place your order.\n5. Upload your reference number\n')
        responded = True
        
    # Return To Main Menu #    
    if '0' in incoming_msg:
        # return image of product and greeting
        msg.media('http://pychat.shirlhost.com/images/product.png')
        msg.body('Thank you for your interest in Mazoyi Mixture. How can I help you?\n\nMAIN MENU\n\n1. What is Mazoyi?\n2. Where can I find Mazoyi?\n3. Mazoyi products & prices.\n4. Place your order.\n5. Upload your reference number\n')
        responded = True     
        
    # What is Mazoyi? #
    if '1' in incoming_msg:
        # return response for Eastern Cape
        msg.body('What is Mazoyi?\n\n\u25AA Mazoyi is complimentary mixture made from aloe as a main ingredient produced by Lwazi Marawu company ca\n\n0. Go back to main menu.') # need to fill this out
        responded = True
        
    # Where can I find Mazoyi? #
    if '2' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which province do you live in?\n\nA. Eastern Cape\nB. Western Cape\nC. Northern Cape\nD. Free State\nE. KwaZulu Natal\nF. Gauteng\nG. Limpopo\nH. Mpumalanga\nI. North West\n\n0. Go back to main menu.') # need to fill this out
        responded = True

    # Cities #    
    if 'a' in incoming_msg:
        # return response for Eastern Cape
        msg.body('Which city are you in or is the closest to you?\n\n6. Centane\n7. Idutywa\n8. UMthatha\n9. Nqamakhwe\n10. Tsomo\n11. Elliotdale\n12. Libode\n13. Tsolo\n14. Qumbu\n15. Queenstown\n16. Mount Frere\n17. East London\n18. eNgcobo\n19. King Williams Town\n20. Alice\n21. Mdantsane\n22. Berlin\n23. Fort Beautfort\n24. Mqanduli\n25. Port St Johns\n26. Lusikisiki\n27. Sterkspruit\n28. Lady Frere\n29. Bizana\n\n0. Return to main menu') # need to fill this out
        responded = True
        
    if 'b' in incoming_msg:
        # return response for Western Cape
        msg.body('Which city are you in or is the closest to you?\n\n30. Paarl 1\n31. Paarl 2\n32. Kraaifotein 2\n33. Makaza\n34. Khayelitsha Site B\n35. Khayelitsha Mall 1\n35. Khayelitsha Mall 2\n36. Khayelitsha Site C\n37. Eerste River\n38. Michielsplein\n39. Town Center\n40. Philippi 2\n41. Philippi-Plaza\n42. Wynberg\n43. Bellville 1\n44. Bellville 2\n45. Mfuleni\n\n0. Return to main menu') # need to fill this out
        responded = True
        
    if 'c' in incoming_msg:
        # return response for Northern Cape
        msg.body('Which city are you in or is the closest to you?\n\n47. Hartwater\n0. Return to main menu') # need to fill this out
        responded = True
        
    if 'd' in incoming_msg:
        # return response for Free State
        msg.body('Which city are you in or is the closest to you?\n\n30. Paarl 1\n31. Paarl 2\n32. Kraaifotein 2\n33. Makaza\n34. Khayelitsha Site B\n35. Khayelitsha Mall 1\n35. Khayelitsha Mall 2\n36. Khayelitsha Site C\n37. Eerste River\n38. Michielsplein\n39. Town Center\n40. Philippi 2\n41. Philippi-Plaza\n42. Wynberg\n43. Bellville 1\n44. Bellville 2\n45. Mfuleni\n\n0. Return to main menu') # need to fill this out
        responded = True
        
    if 'e' in incoming_msg:
        # return response for Western Cape
        msg.body('Which city are you in or is the closest to you?\n\n30. Paarl 1\n31. Paarl 2\n32. Kraaifotein 2\n33. Makaza\n34. Khayelitsha Site B\n35. Khayelitsha Mall 1\n35. Khayelitsha Mall 2\n36. Khayelitsha Site C\n37. Eerste River\n38. Michielsplein\n39. Town Center\n40. Philippi 2\n41. Philippi-Plaza\n42. Wynberg\n43. Bellville 1\n44. Bellville 2\n45. Mfuleni\n\n0. Return to main menu') # need to fill this out
        responded = True
        
    if 'f' in incoming_msg:
        # return response for Western Cape
        msg.body('Which city are you in or is the closest to you?\n\n30. Paarl 1\n31. Paarl 2\n32. Kraaifotein 2\n33. Makaza\n34. Khayelitsha Site B\n35. Khayelitsha Mall 1\n35. Khayelitsha Mall 2\n36. Khayelitsha Site C\n37. Eerste River\n38. Michielsplein\n39. Town Center\n40. Philippi 2\n41. Philippi-Plaza\n42. Wynberg\n43. Bellville 1\n44. Bellville 2\n45. Mfuleni\n\n0. Return to main menu') # need to fill this out
        responded = True
        
    if 'g' in incoming_msg:
        # return response for Western Cape
        msg.body('Which city are you in or is the closest to you?\n\n30. Paarl 1\n31. Paarl 2\n32. Kraaifotein 2\n33. Makaza\n34. Khayelitsha Site B\n35. Khayelitsha Mall 1\n35. Khayelitsha Mall 2\n36. Khayelitsha Site C\n37. Eerste River\n38. Michielsplein\n39. Town Center\n40. Philippi 2\n41. Philippi-Plaza\n42. Wynberg\n43. Bellville 1\n44. Bellville 2\n45. Mfuleni\n\n0. Return to main menu') # need to fill this out
        responded = True
        
    if 'h' in incoming_msg:
        # return response for Western Cape
        msg.body('Which city are you in or is the closest to you?\n\n30. Paarl 1\n31. Paarl 2\n32. Kraaifotein 2\n33. Makaza\n34. Khayelitsha Site B\n35. Khayelitsha Mall 1\n35. Khayelitsha Mall 2\n36. Khayelitsha Site C\n37. Eerste River\n38. Michielsplein\n39. Town Center\n40. Philippi 2\n41. Philippi-Plaza\n42. Wynberg\n43. Bellville 1\n44. Bellville 2\n45. Mfuleni\n\n0. Return to main menu') # need to fill this out
        responded = True
        
    if 'i' in incoming_msg:
        # return response for Western Cape
        msg.body('Which city are you in or is the closest to you?\n\n30. Paarl 1\n31. Paarl 2\n32. Kraaifotein 2\n33. Makaza\n34. Khayelitsha Site B\n35. Khayelitsha Mall 1\n35. Khayelitsha Mall 2\n36. Khayelitsha Site C\n37. Eerste River\n38. Michielsplein\n39. Town Center\n40. Philippi 2\n41. Philippi-Plaza\n42. Wynberg\n43. Bellville 1\n44. Bellville 2\n45. Mfuleni\n\n0. Return to main menu') # need to fill this out
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
