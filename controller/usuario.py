from flask import render_template, request, Blueprint
from config import db
from model.usuario import Usuario

TEMPLATES = "./view"
STATIC = "./static"

usuario_blueprint = Blueprint('usuarios', __name__, template_folder=TEMPLATES, static_folder=STATIC)

@usuario_blueprint.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    nome = request.form.get('nome')
    email = request.form.get('email')

    usuarios = Usuario.query.all()
    for u in usuarios:
        if u.email == email:
            return 'Email já cadastrado!'

    usuario = Usuario(nome, email)
    db.session.add(usuario)
    db.session.commit()
    return 'Usuário cadastrado com sucesso!'

@usuario_blueprint.route('/consultarUsuarios')
def consultarUsuarios():
    usuarios = Usuario.query.all()
    return render_template('listarUsuarios.html', usuarios=usuarios)