from app import db
import json

# TODO: json to dict


class JsonEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    json = db.Column(db.String(), index=False, unique=False)


# def json_entry(func):
#     def wrapper():
#         # ???
#         # self.entry.json  = json.dumps(data)
#         func()
#     return wrapper


class Card:
    def __init__(self, id=None, data=None):
        if id:
            self.entry = JsonEntry.query.get(id)
            self.data = json.loads(self.entry.json)
            if data:
                self.update(data)
        else:
            self.entry = JsonEntry()
            self.entry.json = json.dumps(data)
            self.data = data
        self.id = self.entry.id

    # should we use a decorator?
    # @json_entry
    def update(self, data):
        self.data.__dict__.update(data)
        self.entry.json = json.dumps(self.data)

    def save(self):
        db.session.add(self.entry)
        db.session.commit()

    @classmethod
    def get(cls, id):
        return Card(id=id)

    @classmethod
    def query(cls, expression):
        results = []

        for item in JsonEntry.query.all():
            data = json.loads(item.json)
            for value in data.values():
                if expression in value:
                    results.append(cls.get(item.id))

        return results
