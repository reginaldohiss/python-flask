from flask import Flask, render_template
from config import db
from controller.usuario import usuario_blueprint

TEMPLATES = "./view"
STATIC = "./static"

app = Flask(__name__, static_url_path='', template_folder=TEMPLATES, static_folder=STATIC)
app.register_blueprint(usuario_blueprint)

# Configuração do Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./dados.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

# Definição das Rotas

@app.route('/')
def helloWorld():
    return render_template('login.html')

@app.route('/login', methods={'POST'})
def login():
    return render_template('index.html')

#app.run(host="0.0.0.0", port=5000)
