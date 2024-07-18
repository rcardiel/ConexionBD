from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FormField, SelectField, RadioField, EmailField,IntegerField


class UserForm(Form):
    matricula=IntegerField('Matricula')
    nombre=StringField('Nombre')
    apaterno=StringField('Apaterno')
    email=EmailField('Corro')
    materias=SelectField(choices=[('Español','ESP'),('Mat','Matematicas'),('Ingles','ING')])
    radios=RadioField('cursos', choices=[('1','UNO'),('2','DOS'),('3','TRES')])

