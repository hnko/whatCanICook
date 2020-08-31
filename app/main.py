from flask import Flask, request, redirect
import json

from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

from app.recipes_api_connection import Recipes_API
from app.parser_body import Parser_Body


with open('app/config.json') as file:
    data = json.load(file)
    
    account_sid = data.get('account_sid')
    auth_token = data.get('auth_token')
    my_phone_number = data.get('phone_number')


app = Flask(__name__)

@app.route("/hi", methods=['GET'])
def say_hi():
    return """<!DOCTYPE html><html><body><h1>Hola CaraCola</h1></body></html>"""

@app.route("/sms", methods=['GET', 'POST'])
def get_recipes():
    
    # get body and number from where it is sent
    body = request.values.get('Body', '')
    to = request.values.get('From', '')
    
    
    # create client to send sms
    client = Client(account_sid, auth_token)

    # parse body
    ingredients, dish = Parser_Body(body).parse()

    if not ingredients and not dish:
        client.messages.create(
            body=f"Ups :( \nWe couldn't find results for: {body}",
            to=to,
            from_=my_phone_number
        )
        return 'failing'

    # get recipes
    all_recipes = Recipes_API().get_recipes(ingredients=ingredients, specific_dish=dish)

    # check if there is no result
    if not all_recipes:
        client.messages.create(
            body=f"Ups :( \nWe couldn't find results for the dish: {dish} and the ingredients: {ingredients}",
            to=to,
            from_=my_phone_number
        )
        return 'failing'

    # send all the recipes found, one for sms
   
    for recipe in all_recipes[:3]:
        body_to_send = recipe.title.strip('\n') + '\n' + 'Ingredients: ' + recipe.ingredients + '\n' + recipe.href
        client.messages.create(
            body= body_to_send,
            to=to,
            from_=my_phone_number
        )

    client.messages.create(
        body= 'Thanks for using us! Long life to Twilio!🦉',
        to=to,
        from_=my_phone_number
    )
    return 'success'
    
if __name__ == "__main__":
    app.run(debug=True)