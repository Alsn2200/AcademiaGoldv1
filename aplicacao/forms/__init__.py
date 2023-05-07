from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, equal_to

class FormLogin(FlaskForm):
    usuario = StringField('Usuário', validators=[DataRequired(), length(5, 12)])
    senha = PasswordField('Senha', validators=[DataRequired(), length(6, 18)])
    lembrar = BooleanField('Lembrar-se')
    submit_entrar = SubmitField('Entrar')

class FormCadastrarUsuario(FlaskForm):
    usuario = StringField('Nome de Usuário', validators=[DataRequired(), length(4, 12)])
    nome = StringField('Nome Completo', validators = [DataRequired(),length(1,150)])
    telefone = StringField('Telefone | Whatszapp', validators=[DataRequired(), length(9,14)])
    tipoTreino = StringField('Objetivo', validators=[DataRequired(), length(5,50)])
    pagamento = StringField('Pagamento',validators=[DataRequired(),length(1,50)])
    senha = PasswordField('Senha', validators=[DataRequired(), length(6, 18)])
    confirmacao = PasswordField('Confirmação de Senha', validators=[DataRequired(), equal_to('senha')])
    submit_criar = SubmitField('Cadastrar')