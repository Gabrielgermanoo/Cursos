from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SubmitField
from wtforms.validators import DataRequired


class CursoForm(FlaskForm):
  curso = StringField('Curso', validators=[DataRequired()])
  tipo = IntegerField('tipo', validators=[DataRequired()])
  duracao = DecimalField('Duração', places=1)
  submit = SubmitField('Salvar')