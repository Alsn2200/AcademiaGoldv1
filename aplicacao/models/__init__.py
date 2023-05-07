from aplicacao import database

class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    usuario = database.Column(database.String, nullable=False)
    nome = database.Column(database.String, nullable=False)
    telefone = database.Column(database.String, nullable=False)
    tipoTreino = database.Column(database.String, nullable=False)
    pagamento = database.Column(database.String, nullable=False)
    senha = database.Column(database.String, nullable=False)