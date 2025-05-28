from peewee import Model, CharField, DateTimeField
from database.database import db_proxy
import datetime


class Cliente(Model):
    nome = CharField()
    email = CharField()
    idade = CharField()
    cidade= CharField()
    data_registro=DateTimeField(default=datetime.datetime.now)

    class Meta:
        db = db_proxy