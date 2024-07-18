from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FormField, SelectField, RadioField, EmailField,IntegerField
from wtforms import validators

class UserForm(Form):
    matricula=IntegerField('Matricula')
    nombre=StringField('Nombre')
    apaterno=StringField('Apaterno')
    email=EmailField('Corro')
    materias=SelectField(choices=[('Español','ESP'),('Mat','Matematicas'),('Ingles','ING')])
    radios=RadioField('cursos', choices=[('1','UNO'),('2','DOS'),('3','TRES')])


class UserForm2(Form):
     id=IntegerField('id')
     nombre=StringField('Nombre',[
        validators.DataRequired(message='El Nombre es requerido')
    ])
     apaterno=StringField('Apaterno',[
        validators.DataRequired(message='El apellido es requerido')
    ])
     amaterno=StringField('Apaterno',[
        validators.DataRequired(message='El apellido es requerido')
    ])
     email=EmailField('Corro',[
        validators.DataRequired(message='El correo es requerido'),
        validators.Email(message='Ingrese un correo valido')
    ])