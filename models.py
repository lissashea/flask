from peewee import *

db = SqliteDatabase('books.db')

class Book(Model):
    title = CharField()
    author = CharField()
    year = IntegerField()

    class Meta:
        database = db

def initialize_db():
    db.connect()
    db.create_tables([Book], safe=True)
