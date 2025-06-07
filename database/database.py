from peewee import PostgresqlDatabase, Proxy
import os
from dotenv import load_dotenv
from models.clientedb import db_proxy

load_dotenv()


def init_db():
    db= PostgresqlDatabase(
        (os.getenv('db_name')),
        user=os.getenv('db_user'),
        password=os.getenv('db_password'),
        host=os.getenv('db_host'),

)
    db_proxy.initialize(db)
    return db
