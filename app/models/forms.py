from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired


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

class EditProfileForm(FlaskForm):
  user = StringField('Nome do usuário', validators=[DataRequired()])
  password = PasswordField('Senha', validators=[DataRequired()])
  name = StringField('Nome')