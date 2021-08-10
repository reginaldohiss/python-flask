from config import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(256))
    email = db.Column(db.String(128), unique=True)

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    def __repr__(self):
        return 'Usuário: ' + self.nome + ' | ' + self.email