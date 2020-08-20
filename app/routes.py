from app import app
from app.models import Card
from flask import render_template, jsonify, redirect, request

# import requests
from random import *
import json


@app.route("/api/cards/search/<string:expression>", methods=["GET"])
def search(expression):
    cards = Card.query_from_string(expression)
    return jsonify(cards)


@app.route("/api/cards/<int:card_id>", methods=["GET", "POST"])
def card(card_id):
    if request.method == "GET":
        card = Card.query.get(card_id)
        return jsonify(card.to_dict())
        # return jsonify(card)

    elif request.method == "POST":
        card = Card.query.get(card_id)
        data = request.form

        card.json_data = json.dumps(request.form)
        card.save()
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    if app.debug:
        return redirect("http://localhost:8080/{}".format(path), code=302)
    return render_template("index.html")
