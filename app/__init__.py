from flask import Flask
# from app import cli
import os
from app.elastic import Card
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Index

ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
connections.create_connection(hosts=[ELASTICSEARCH_URL], timeout=20)

Index(Card).create(ignore=400)
print('Index "cards" created.')

a = Card(title='Titre 1', text="Texte 1")
a.save()
b = Card(title='Titre 2', text="Texte 2")
b.save()
print("Created sample data")

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")


# @app.shell_context_processor
# def make_shell_context():
#     return {'elastic': elastic, 'User': User, 'Post': Post}

from app import routes

