from flask import Flask
from configuration import configurar_tudo

app= Flask(__name__)


configurar_tudo(app)

from models.clientedb import Cliente
app.run(debug= True)