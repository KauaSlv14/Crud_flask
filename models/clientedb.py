from peewee import Model, CharField, DateTimeField
from database.database import db
import datetime


class Cliente(Model):
    nome = CharField()
    email = CharField()
    idade = CharField()
    cidade= CharField()
    data_registro=DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db 