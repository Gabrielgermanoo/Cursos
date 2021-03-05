from app import app
from flask import request, render_template, redirect, url_for
from app.models.forms import CursoForm
from app.models.cursos import Curso
from app import db


@app.route("/cursos")
def cursos():
  cursos = Curso.query.all()
  return render_template("cursos.html", cursos=cursos)

@app.route("/cursos/novo", methods=['GET', 'POST'])
def novo_curso():
  form = CursoForm()
  if form.validate_on_submit():
    f = Curso(curso=form.nome.data, tipo=form.tipo.data,
      duracao=form.duracao.data)
    db.session.add(f)
    db.session.commit()
    return redirect(url_for("cursos"))
  return render_template("cursos_cadastro.html", form=form)