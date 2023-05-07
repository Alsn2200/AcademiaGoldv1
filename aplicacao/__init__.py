from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '71110f84ca2b997e67ce349dee70afd3'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///academiagold.db'




database = SQLAlchemy(app)
bcrypt = Bcrypt(app)




from aplicacao import routers