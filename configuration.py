from flask import Flask
from routes.home import home_route
from routes.clientes import home_clientes
from database.database import init_db

def configurar_tudo(app):
    configurar_banco()
    configurar_routes(app)

def configurar_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(home_clientes, url_prefix='/clientes')



def configurar_banco():
    db= init_db()
    from models.clientedb import Cliente
    if db.is_closed():
        db.connect()
    db.create_tables([Cliente]) 



