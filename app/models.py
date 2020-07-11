from app import db
import json
import logging

# TODO: json to dict


class JsonEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    json = db.Column(db.String(), index=False, unique=False)

class Card(dict):
    def __init__(self, id=None, data=None):
        if id:
            entry = json.loads(JsonEntry.query.get(id).json)
            self = {'id':id, **entry.json}
            if data:
                self.update(data)
        else:
            entry = JsonEntry()
            entry.json = json.dumps(data)
            self = {'id':entry.id, **entry.json}
        return

    def update(self, data):
        self.__dict__.update(data)

    def save(self):
        entry = JsonEntry.query.get(self['id'])
        entry.json = json.dumps(self.__dict__)
        # entry.json = json.dumps(self)
        db.session.add(entry)
        db.session.commit()

    @classmethod
    def get(cls, id):
        return {'id':id, **JsonEntry.query.get(id=id).json}

    @classmethod
    def query(cls, expression):
        results = []
        all_entries = JsonEntry.query.all()
        for item in all_entries:
            data = json.loads(item.json)
            for value in data.values():
                if expression in value:
                    # results.append(item.json))
                    results.append(data)
                    # results.append(cls.get(item.id))

        return results
