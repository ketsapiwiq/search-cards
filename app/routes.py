from app import app
from app.models import Card
from flask import render_template, jsonify, redirect, request

# import requests
from random import *
import json


@app.route('/api/cards/search/', defaults={'expression': ''}, methods=["GET"])
@app.route("/api/cards/search/<string:expression>", methods=["GET"])
def search(expression):
    cards = Card.query_from_string(expression)
    return jsonify(cards)

@app.route('/api/cards/', defaults={'card_id': ''}, methods=["POST"])
@app.route("/api/cards/<int:card_id>", methods=["GET", "POST"])
def card(card_id):
    if request.method == "GET":
        card = Card.query.get(card_id)
        return jsonify(card.to_dict())
        # return jsonify(card)

    elif request.method == "POST":
        request_data = request.form
        if(card_id)=='':
            create = True

        # /!\ No sanitization, should slug the keys and bleach the value/content
        data = request.form

        if not data and create:
            return '', 204 # No operation
        if create:
        # /!\ Or sanitization in the function
            card = Card(data)
        else:
            if not data:
                Card.delete(card_id)
                return json.dumps({'success':True, 'deleted':True, 'id':card.id}), 200, {'ContentType':'application/json'} 
            card = Card.query.get(card_id)
            card.json_data = json.dumps(request.form)
        card.save()
        return json.dumps({'success':True, 'created':create}), 200, {'ContentType':'application/json'} 


@app.route("/<path:path>")
@app.route("/", defaults={"path": ""})
def catch_all(path):
    if app.debug:
        return redirect("http://localhost:8080/{}".format(path), code=302)
    return render_template("index.html")
