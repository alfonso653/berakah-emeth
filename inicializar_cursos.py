"""
Script para inicializar cursos en la base de datos
"""
from app import app, db
from models import Curso

with app.app_context():
    # Verificar si ya existen cursos
    if Curso.query.count() == 0:
        cursos = [
            Curso(
                nombre="Fundamentos Bíblicos I",
                slug="fundamentos-biblicos-1",
                descripcion="Introducción a los fundamentos de la fe cristiana y el estudio bíblico.",
                activo=True
            ),
            Curso(
                nombre="Teología Sistemática",
                slug="teologia-sistematica",
                descripcion="Estudio sistemático de las doctrinas bíblicas fundamentales.",
                activo=True
            ),
            Curso(
                nombre="Historia de la Iglesia",
                slug="historia-iglesia",
                descripcion="Recorrido histórico del cristianismo desde sus inicios hasta la actualidad.",
                activo=True
            ),
            Curso(
                nombre="Hermenéutica Bíblica",
                slug="hermeneutica-biblica",
                descripcion="Principios y métodos para la interpretación correcta de las Escrituras.",
                activo=True
            ),
            Curso(
                nombre="Doctrina de la Revelación",
                slug="doctrina-revelacion",
                descripcion="Estudio profundo sobre la revelación general y especial de Dios.",
                activo=True
            )
        ]
        
        for curso in cursos:
            db.session.add(curso)
        
        db.session.commit()
        print(f"✅ Se crearon {len(cursos)} cursos correctamente")
    else:
        print(f"ℹ️ Ya existen {Curso.query.count()} cursos en la base de datos")
