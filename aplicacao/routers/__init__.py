from aplicacao import app, database, bcrypt
from flask import redirect, render_template, url_for, flash
from aplicacao.forms import FormLogin, FormCadastrarUsuario
from aplicacao.models import Usuario
from flask_login import login_user, logout_user, login_required


@app.route('/', methods=['GET', 'POST'])
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/login')
def login():
    form = FormLogin()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(usuario=form.usuario.data).first()
        if user and bcrypt.check_password_hash(user.senha, form.senha.data):
            login_user(user, remember=form.lembrar.data)
            flash(f'Login feito com sucesso para o user: {form.usuario.data}', 'alert alert-success')
            return redirect(url_for('index'))
        else:
            flash(f'Usuário ou senha inválidos', 'alert alert-danger')

    return render_template('login.html', form=form)
@app.route('/cadastro')
def cadastro():
    form = FormCadastrarUsuario()
    if form.validate_on_submit():
        senha_crypto = bcrypt.generate_password_hash(form.senha.data)
        print(f'senha {form.senha.data}')
        print(f'senha criptografada {senha_crypto}')
        try:
            user = Usuario(usuario=form.usuario.data, telefone=form.telefone.data,tipoTreino=form.tipoTreino.data,pagamento=form.pagamento.data, senha=senha_crypto)
            database.session.add(user)
            database.session.commit()
            flash(f'Usuário cadastrado com sucesso', 'alert alert-success')
            return redirect('login')
        except:
            flash(f'Não foi possível cadastrar usuário', 'alert alert-danger')
    return render_template('cadastro.html', form=form)
@app.route('/index')
def index():
    return render_template('index.html')