from flask import Flask,render_template, request, url_for
from flask_material import Material

import forms
app=Flask(__name__)
Material(app)

@app.route("/")#rutas
def index():
    titulo="Index de Titulo"
    lista=['Mario','Pedro','Juan']
    return render_template("index.html",titulo=titulo,lista=lista)


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
    app.run(debug=True)