from app import app, db, login_manager
from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.forms import CursoForm
from app.models.forms import LoginForm
from app.models.forms import UserForm
from app.models.forms import DeleteForm
from app.models.cursos import Curso
from app.models.users import User
from werkzeug.security import generate_password_hash

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
@login_required
def perfil():
  return render_template("perfil.html", perfil=perfil)

@app.route("/perfil/<id>/editar", methods=["GET", "POST"])
def editar_perfil(id):
  form = UserForm()
  user = User.query.get(id)
  if user is None:
    return abort (404)
  if form.validate_on_submit():
      user.user = form.user.data
      user.password = generate_password_hash(form.password.data)
      user.name = form.name.data
      user.email = form.email.data
      db.session.commit()
      return redirect(url_for("perfil"))
  return render_template("editar_cad.html", form=form, user=user)

@app.route("/cursos/novo", methods=['GET', 'POST'], defaults={"user": None})
@app.route("/cursos/novo/<user>")
@login_required
def novo_curso(user):
  form = CursoForm()
  if form.validate_on_submit():
    f = Curso(curso=form.curso.data, tipo=form.tipo.data,
      duracao=form.duracao.data)
    db.session.add(f)
    db.session.commit()
    return redirect(url_for("cursos"))
  return render_template("cursos_cadastro.html", form=form, user=user)

@app.route("/cursos/<id>/editar", methods=["GET", "POST"])
@login_required
def editar_curso(id):
  form = CursoForm()
  curso = Curso.query.get(id)
  if curso is None:
    return abort (404)
  if form.validate_on_submit():
    curso.curso = form.curso.data
    curso.tipo = form.tipo.data
    curso.duracao = form.duracao.data
    db.session.commit()
    return redirect(url_for("cursos"))
  return render_template("editar_curso.html", form=form, curso=curso)

@app.route("/cursos/<id>/excluir", methods=["GET", "POST"])
def excluir_curso(id):
  form = DeleteForm()
  curso = Curso.query.get(id)
  if curso is None:
    return abort(404)
  if form.validate_on_submit():
    db.session.delete(curso)
    db.session.commit()
    return redirect (url_for("cursos"))
  return render_template("curso_excluir.html", form=form, curso = curso)

@app.route("/logout")
def logout():
  logout_user()
  return redirect(url_for("inicio"))
