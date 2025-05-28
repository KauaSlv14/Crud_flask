from flask import Flask, Blueprint, render_template, request, url_for, request
from models.clientedb import Cliente
home_clientes = Blueprint('clientes', __name__)
#passo a passo:

# def de formulario de login = GET
@home_clientes.route('/novo')
def form_clientes():
    return render_template('form_clientes.html')

#editar cliente/editar=GET

@home_clientes.route('/<int:cliente_id>/editar')
def editar_clientes(cliente_id):
    cliente=Cliente.get(Cliente.id == cliente_id)

    return render_template('form_clientes.html', cliente=cliente)
    

# criar def de listar clientes = GET
@home_clientes.route('/')
def listar_clientes():
    clientes=Cliente.select()
    return render_template("listar_clientes.html", clientes=clientes)

# criar def de adicionar cliente/aicionar, inserir clientes novos no banco de dados = POST
@home_clientes.route('/', methods=['POST'])
def adicionar_clientes():
    data=request.json
    
    novo_usuario =Cliente.create(
        nome=data['nome'],
        idade=data['idade'],
        email=data['email'],
        cidade=data['cidade']
    )
    return render_template('item.html', cliente=novo_usuario)



#criar def de atualizar cliente/atualizar= PUT
@home_clientes.route('/<int:cliente_id>/atualizar', methods=['PUT'])
def atualizar_clientes(cliente_id):
    data =request.json
    
    cliente_editado = Cliente.get(Cliente.id == cliente_id)
    cliente_editado.nome = data['nome']
    cliente_editado.idade = data['idade']
    cliente_editado.email = data['email']
    cliente_editado.cidade = data['cidade']
    cliente_editado.save()

    #obter dados do clliente para editar
    

    return render_template('item.html', cliente=cliente_editado)

#criar def de deletear cliente/delete= DELETE

@home_clientes.route('/<int:cliente_id>/delete', methods=['DELETE'])
def delete_clientes(cliente_id):
    cliente = Cliente.get(Cliente.id == cliente_id)
    cliente.delete_instance()
    return render_template('item.html', cliente=cliente)

@home_clientes.route('/<int:cliente_id>')
def detalhes_cliente(cliente_id):
    cliente=Cliente.get(Cliente.id == cliente_id)
    return render_template('detalhes_cliente.html', cliente=cliente)