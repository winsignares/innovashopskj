from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from config.db import db, app
from models.EmpresaModel import EMP, EMPSchema

ruta_empresa = Blueprint('ruta_empresa', __name__)

EMP_schema = EMPSchema() 
EMPS_schema = EMPSchema(many=True) 

@app.route('/empresas/crear', methods=['POST'])
def crear_empresa():
    if request.method == 'POST':
        
        nombre = request.form['name_emp']
        mail = request.form['mail_emp']
        ubicacion = request.form['ubicacion']
        status = request.form['status']
        IVA = int(request.form['IVA'])  
        fecha_inicio = request.form['fecha_Inicio']
        fecha_final = request.form['fecha_final']

        nueva_empresa = EMP(
            name_emp=nombre,
            mail_emp=mail,
            ubicacion=ubicacion,
            status=status,
            IVA=IVA,
            fecha_Inicio=fecha_inicio,
            fecha_final=fecha_final
        )

        db.session.add(nueva_empresa)
        db.session.commit()

    return redirect('/empresas')


@app.route('/empresas', methods=['GET'])
def ver_empresas():
    empresas = EMP.query.all()
    return render_template('./Admin/portalAdministrativo.html', empresas=empresas)

@app.route('/Portal_Empresa', methods=['GET'])
def portalempresa():
    
    if 'usuario' in session:
        return render_template("./Portales/Portal_Empresa.html", usuario = session['usuario'])
    else:
        return redirect('/')


