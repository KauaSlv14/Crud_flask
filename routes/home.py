from flask import Flask, Blueprint, render_template
home_route= Blueprint('home', __name__)
from models.clientedb import Cliente
@home_route.route('/')

def home():
      return render_template('index.html', clientes=Cliente)