from peewee import PostgresqlDatabase
import os
from dotenv import load_dotenv

load_dotenv()

db= PostgresqlDatabase(
    db_name=os.getenv('db_name'),
    user=os.getenv('db_user'),
    password=os.getenv('db_password'),
    host=os.getenv('db_host'),

)
