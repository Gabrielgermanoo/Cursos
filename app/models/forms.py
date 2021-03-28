from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField, BooleanField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired

class DeleteForm(FlaskForm):
  submit = SubmitField('Deletar')

class CursoForm(FlaskForm):
  curso = StringField('curso', validators=[DataRequired()])
  tipo = StringField('tipo', validators=[DataRequired()])
  duracao = IntegerField('Duração', validators=[DataRequired()])
  submit = SubmitField('Salvar')

class LoginForm(FlaskForm):
  username = StringField ('username', validators= [DataRequired()])
  password = PasswordField ('password', validators=[DataRequired()])
  remember_me = BooleanField ('remember_me')

class UserForm(FlaskForm):
  user = StringField('Nome do usuário', validators=[DataRequired()])
  password = PasswordField ('Senha', validators=[DataRequired()])
  name = StringField ('Nome', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired()])
  submit = SubmitField('Criar')

class ProfessorForm(FlaskForm):
  nome = StringField ('Nome', validators=[DataRequired()])
  data_nascimento = DateField ('Data de Nascimento')
  formacao = StringField ('Formação')
  submit = SubmitField ('Salvar')
 
class AvaliacaoForm(FlaskForm):
  estrela1 = SubmitField('⭐')
  estrela2 = SubmitField('⭐')
  estrela3 = SubmitField('⭐')
  estrela4 = SubmitField('⭐')
  estrela5 = SubmitField('⭐')