from app import app, db, login_manager
from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from app.models.forms import CursoForm
from app.models.forms import LoginForm
from app.models.forms import UserForm
from app.models.cursos import Curso
from app.models.users import User

@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.errorhandler(404)
def not_found_error(error):
  return render_template("404.html"), 404

@app.errorhandler(500)
def not_found_error(error):
  db.session.rollback()
  return render_template("500.html"), 500

@app.route("/", defaults={"user": None})
@app.route("/index/<user>")
def inicio(user):
  return render_template("index.html", user = user)

@app.route("/cursos", defaults={"user": None})
@app.route("/cursos/<user>")
def cursos(user):
  cursos = Curso.query.all()
  return render_template("cursos.html", cursos=cursos, user=user)

@app.route("/avaliacoes", defaults={"user": None})
@app.route("/avaliacoes/<user>")
def avaliacoes(user):
  return render_template ("avaliacoes.html", avaliacoes=avaliacoes, user = user)

@app.route("/cadastro",  methods=['GET', 'POST'])
def cadastro():
  form = UserForm()
  if form.validate_on_submit():
    n = User(username=form.user.data, password=form.password.data,
     name=form.name.data,
     email=form.email.data)
    db.session.add(n)
    db.session.commit()
    return redirect(url_for("login"))
  return render_template("cadastro.html", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user and user.check_password(form.password.data):
      login_user (user)
      flash("Autenticado")
      return redirect(url_for("inicio"))
    else:
      flash("Login Inválido")
  return render_template("login.html", form=form)

@app.route("/perfil")
def perfil():
  return render_template("perfil.html", perfil=perfil)

@app.route("/perfil/editar")
def editar_perfil():
  return render_template("editar_cad.html")

@app.route("/cursos/novo", methods=['GET', 'POST'], defaults={"user": None})
@app.route("/cursos/novo/<user>")
def novo_curso(user):
  form = CursoForm()
  if form.validate_on_submit():
    f = Curso(curso=form.curso.data, tipo=form.tipo.data,
      duracao=form.duracao.data)
    db.session.add(f)
    db.session.commit()
    return redirect(url_for("cursos"))
  return render_template("cursos_cadastro.html", form=form, user=user)

@app.route("/logout")
def logout():
  logout_user()
  return redirect(url_for("inicio"))