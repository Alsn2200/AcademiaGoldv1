from aplicacao import app, database, bcrypt
from aplicacao.models import Usuario

'''cria a database'''
# with app.app_context():
#     database.create_all()

'''Apaga e cria novamente a database'''

# with app.app_context():
#     database.drop_all()
#     database.create_all()

'''Insere um usuário inicial na base de dados'''
with app.app_context():
    senha_crypto = bcrypt.generate_password_hash('123456')
    user = Usuario(usuario='admin', nome='aaaa',telefone='7512345678',tipoTreino='Hipertrofia', pagamento='pix', senha=senha_crypto)
    database.session.add(user)
    database.session.commit()

#Realiza um selecta em toda a tabela
# with app.app_context():
#     usuarios = Usuario.query.all()
#     for item in usuarios:
#         print(f'{item.usuario}, {item.email}, {item.senha}, {item.id}')

# with app.app_context():
#     user = Usuario.query.filter_by(id=2).first()
#     print(user.usuario)
#     database.session.delete(user)
#     database.session.commit()