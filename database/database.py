from peewee import PostgresqlDatabase, Proxy
import os
from dotenv import load_dotenv

load_dotenv()

db_proxy= Proxy()

def init_db():
    db= PostgresqlDatabase(
        os.getenv('db_name'),
        user=os.getenv('db_user'),
        password=os.getenv('db_password'),
        host=os.getenv('db_host'),

)
    db_proxy.initialize(db)
    return db_proxy
