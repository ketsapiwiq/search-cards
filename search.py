from app import app, db
from app.models import Card


a = Card(data=dict(title="Apple",text="This is an apple"))
a.save()
b = Card(data=dict(title="Pear",text="A pear"))
b.save()
print("Created sample data")
