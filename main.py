from flask import Flask,render_template, request, url_for, redirect
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
        mensaje='Registro Nuevo'
        flash(mensaje)
        return redirect(url_for('ABCompleto'))
    
    return render_template("alumnos.html",form=alum_form)
     
@app.route("/eliminar",methods=['GET','post'])
def eliminar():
    
    alum_form=forms.UserForm2(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        #alum1=select * from alumnos where id==id
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum_form.id.data=request.args.get('id')
        alum_form.nombre.data=alum1.nombre
        alum_form.apaterno.data=alum1.apaterno
        alum_form.amaterno.data=alum1.apaterno
        alum_form.email.data=alum1.email
        
    if request.method=='POST':
        id=alum_form.id.data
        alum = Alumnos.query.get(id)
        db.session.delete(alum) 
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    
    return render_template("eliminar.html",form=alum_form)
    
@app.route("/ABC_Completo",methods=['GET','POST'])
def ABCompleto():
    create_form=forms.UserForm2(request.form)
    alumno=Alumnos.query.all()
    return render_template('ABC_Completo.html',form=create_form,alumno=alumno)


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