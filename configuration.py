from flask import Flask
from routes.home import home_route
from routes.clientes import home_clientes
from database.database import db
from models.clientedb import Cliente

def configurar_tudo(app):
    configurar_routes(app)
    configurar_banco()

def configurar_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(home_clientes, url_prefix='/clientes')



def configurar_banco():
    if db.is_closed():
        db.connect()
    db.create_tables([Cliente]) 



