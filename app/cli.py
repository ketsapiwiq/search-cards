from os
import click
from elasticsearch_dsl import Index
from flask.cli import with_appcontext

@with_appcontext
@click.command('elastic')
@click.argument('index_name')
def create(index_name):
    index = Index(name=index_name)
    # import pudb; pudb.set_trace()
    index.settings(number_of_shards=1, number_of_replicas=0)
    index.create()
    print('Index '+str(index_name)+' created.')