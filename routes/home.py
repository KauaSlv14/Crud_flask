from flask import Flask, Blueprint, render_template
home_route= Blueprint('home', __name__)
@home_route.route('/')

def home():
      from models.clientedb import Cliente
      return render_template('index.html', clientes=Cliente)