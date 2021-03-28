from app import app, db, login_manager
from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.forms import CursoForm
from app.models.forms import LoginForm
from app.models.forms import UserForm
from app.models.forms import DeleteForm
from app.models.forms import ProfessorForm
from app.models.forms import AvaliacaoForm
from app.models.cursos import Curso
from app.models.prof import Professor
from app.models.users import User
from app.models.avaliacao import Avaliacao
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


# Avaliar
@app.route("/cursos/<id>/avaliar", methods=["GET", "POST"])
def avaliacoes(id):
  form = AvaliacaoForm()
  curso = Curso.query.get(id)
  if curso is None:
    return abort(404)
  if form.validate_on_submit():
    if form.estrela1.data:
      estrelas = 1
    if form.estrela2.data:
      estrelas = 2
    if form.estrela3.data:
      estrelas = 3
    if form.estrela4.data:
      estrelas = 4
    if form.estrela5.data:
      estrelas = 5
    a = Avaliacao(estrelas = estrelas, curso_id = id)
    db.session.add(a)
    db.session.commit()
    return redirect (url_for("cursos"))
  return render_template ("avaliacoes.html", avaliacoes=avaliacoes, form = form, curso = curso)

# Professor
@app.route("/professores/novo", methods=['GET', 'POST'])
@login_required
def novo_professor():
  form = ProfessorForm()
  if form.validate_on_submit():
    a = Professor(nome = form.nome.data,
    data_nascimento = form.data_nascimento.data,
    formacao = form.formacao.data)
    db.session.add(a)
    db.session.commit()
    return redirect (url_for("professores"))
  return render_template("prof_cadastro.html", form = form)

@app.route("/professores")
def professores():
  professores = Professor.query.all()
  return render_template ("professores.html", professores = professores)

@app.route("/professores/<id>/editar", methods=["GET", "POST"])
def editar_professor(id):
  form = ProfessorForm()
  professor = Professor.query.get(id)
  if professor is None:
    return abort(404)
  if form.validate_on_submit():
    professor.nome = form.nome.data
    professor.data_nascimento = form.data_nascimento.data
    professor.formacao = form.formacao.data
    db.session.commit()
    return redirect(url_for("professores"))
  return render_template("professor_edicao.html", form = form, professor = professor)

@app.route("/professores/<id>/excluir", methods = ["POST", "GET"])
def excluir_professor(id):
  form = DeleteForm()
  professor = Professor.query.get(id)
  if professor is None:
    return abort(404)  
  if form.validate_on_submit():
    db.session.delete(professor)
    db.session.commit()
    return redirect(url_for("professores"))
  return render_template("professor_exclusao.html", form = form, professor = professor)


#Login
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


#perfil (CRUD)
@app.route("/perfil")
@login_required
def perfil():
  return render_template("perfil.html", perfil=perfil)

@app.route("/perfil/<id>/editar", methods=["GET", "POST"])
def editar_perfil(id):
    form = UserForm()
    user = User.query.get(id)
    if user is None:
      return abort(404)
    if form.validate_on_submit():
        user.user = form.user.data
        user.password = generate_password_hash(form.password.data)
        user.name = form.name.data
        user.email = form.email.data
        if username is not None:
          flash("Usuário já cadastrado, por favor coloque outro nome.")
        db.session.commit()
        return redirect(url_for("perfil"))
    return render_template("editar_cad.html", form=form, user=user)


#Cursos 
@app.route("/cursos", defaults={"user": None})
@app.route("/cursos/<user>")
def cursos(user):
  cursos = Curso.query.all()
  return render_template("cursos.html", cursos=cursos, user=user)

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
    return abort(404)
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

@app.route("/cursos/<id>/professores", methods=["GET", "POST"])
def lista_professores(id):
  curso = Curso.query.get(id)
  professores = Professor.query.all()
  if curso is None:
    return abort(404)
  return render_template("lista_professores.html",
    curso = curso, professores = professores)
  
@app.route("/cursos/<curso_id>/cursos_professores/<professor_id>/adicionar")
def adicionar_lista_professores(curso_id, professor_id):
  curso = Curso.query.get(curso_id)
  professor = Professor.query.get(professor_id)
  if curso is None or professor is None:
    return abort(404)
  curso.cursos_prof.append(professor)
  db.session.commit()
  return redirect(url_for("lista_professores", id=curso_id))

@app.route("/cursos/<curso_id>/cursos_professores/<professor_id>/remover")
def remover_lista_professores(curso_id, professor_id):
  curso = Curso.query.get(curso_id)
  professor = Professor.query.get(professor_id)
  if curso is None or professor is None:
    return abort(404)
  curso.cursos_prof.remove(professor)
  db.session.commit()
  return redirect(url_for("lista_professores", id=curso_id))


#logout
@app.route("/logout")
def logout():
  logout_user()
  return redirect(url_for("inicio"))



#admin
@app.route("/perfil/admin")
def adm_edit():
  user = User.query.all()
  return render_template("admin_edit.html", user=user)

@app.route("/perfil/admin/<id>/excluir", methods=["GET", "POST"])
@login_required
def adm_excluir(id):
  form = DeleteForm()
  user = User.query.get(id)
  if user is None:
    return abort(404)
  if form.validate_on_submit():
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("adm_edit"))
  return render_template("user_excluir.html", form=form, user = user)