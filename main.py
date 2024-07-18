from flask import Flask,render_template, request, url_for
from flask_material import Material

from flask_wtf.csrf import CSRFProtect

from config import DevelopmentConfig

from flask import g
from flask import flash

from models import db

from models import Alumnos

import forms
app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
Material(app)
csrf=CSRFProtect()

@app.route("/")#rutas
def index():
    titulo="Index de Titulo"
    lista=['Mario','Pedro','Juan']
    return render_template("index.html",titulo=titulo,lista=lista)


@app.route("/alumnos",methods=['GET','post'])
def alumnos():
    
    alum_form=forms.UserForm2(request.form)
    
    if request.method=='POST':
        alum=Alumnos(nombre=alum_form.nombre.data,
                     apaterno=alum_form.apaterno.data,
                     amaterno=alum_form.amaterno.data,
                     email=alum_form.email.data) 
        db.session.add(alum)
        db.session.commit()
    
    return render_template("alumnos.html",form=alum_form)
     
    



@app.route("/usuarios",methods=['GET','post'])
def usuarios():
    num1=0
    num2=0
    alum_form=forms.UserForm(request.form)
    
    if request.method=='POST':
        mat=alum_form.matricula.data
        nom=alum_form.nombre.data
        apa=alum_form.apaterno.data
        mat=alum_form.materias.data
        rad=alum_form.radios.data   
        return render_template("usuarios.html",form=alum_form,mat=mat,nom=nom,apa=apa,rad=rad)
     
    return render_template("usuarios.html",form=alum_form)

    
    
    
if __name__=="__main__":
    csrf.init_app(app)
    db.init_app(app)
    
    with app.app_context():
          db.create_all()
    app.run()