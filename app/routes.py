from app import app
from app.elastic import Card
from flask import render_template, jsonify
# import requests
from random import *


@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)

@app.route('/api/cards/<string:query>', methods=['GET'])
def cards(query):
    # response = { 'cards': [{'title':'Titre 1', 'text':'Texte 1'},{'title':'Titre 2', 'text':'Texte 2'}] }
    cards = Card.get_cards(query)
    return jsonify(cards)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # if app.debug:
    #     return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")