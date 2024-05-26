from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from config.db import app, db
from models.EmpresaModel import EMP

def create_new_company_db(company_name):
    database_name = f"company_{company_name.lower()}"

    base_connection_string = 'mysql+pymysql://root:root@127.0.0.1/'

    engine = create_engine(base_connection_string + database_name)

    if not database_exists(engine.url):
        create_database(engine.url)

    return engine

def create_company(name, mail_emp, ubicacion, status, fecha_inicio, fecha_final, user, password):
    try:
        engine = create_new_company_db(name)

        # Create the tables in the new database
        with engine.connect() as connection:
            connection.execute(f"CREATE SCHEMA IF NOT EXISTS {name};")
            connection.execute(f"USE {name};")
            with app.app_context():
                db.create_all(bind=engine)

        new_company = EMP(name_emp=name, mail_emp=mail_emp, ubicacion=ubicacion, status=status,
                          fecha_Inicio=fecha_inicio, fecha_final=fecha_final, user=user, password=password)

        db.session.add(new_company)
        db.session.commit()

        return new_company
    
    except Exception as e:
        print(f"Error al crear la empresa: {e}")
        return None