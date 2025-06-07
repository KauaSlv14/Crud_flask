from peewee import Model, CharField, DateTimeField, Proxy
import datetime

db_proxy = Proxy()

class Cliente(Model):
    nome = CharField()
    email = CharField()
    idade = CharField()
    cidade= CharField()
    data_registro=DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db_proxy