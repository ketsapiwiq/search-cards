from app import db
import json
from flask import jsonify
import logging

# class Card(db.Model, dict):
class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    json_data = db.Column(db.String(), index=False, unique=False)

    def __init__(self, data):
        self.json_data = json.dumps(data)

    def update_from_dict(self, data):
        original_data = json.loads(self.json_data)
        new_data = original_data.update(data)
        self.json_data = json.dumps(new_data)
        self.save()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return dict(id=self.id, data=json.loads(self.json_data))
        # return dict(id=self.id, data=self.json_data) # json data as escaped string

    @classmethod
    def query_from_string(cls, expression):
        cards = []

        if expression == "":
            results = cls.query.all()
        else:
            results = cls.query.filter(cls.json_data.contains(expression))
        for result in results:
            # cards.append(dict(id=result.id, data=json.loads(result.json_data)))
            cards.append(result.to_dict())
        return cards
