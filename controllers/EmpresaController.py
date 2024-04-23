from flask import Blueprint, render_template, request, redirect
from config.db import app, db, ma
from models.EmpresaModel import EMP, EMPSchema

ruta_empresa = Blueprint('route_empresa', __name__)

EMP_schema = EMPSchema()
EMP_schema = EMPSchema(many=True)


