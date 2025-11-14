from flask_sqlalchemy import SQLAlchemy
from models import db, Usuario, ClaseCompletada
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_mail import Mail, Message
from functools import wraps

app = Flask(__name__)
# Usar SQLite para desarrollo local, PostgreSQL para producción
import os
if os.environ.get('RAILWAY_ENVIRONMENT'):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:uoLTdxMcdpriiVvMsplZQDpWdEUIrVTB@postgres.railway.internal:5432/railway'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///berakah.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'clave-secreta-muy-segura'
# Configuración del correo
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'documentosbiblicos3@gmail.com'
app.config['MAIL_PASSWORD'] = 'wsze sgcm issk vcns'

mail = Mail(app)

db.init_app(app)

# Decorador para proteger rutas
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario_id' not in session:
            flash('⚠️ Debes iniciar sesión para acceder a esta sección.')
            return redirect(url_for('login_form'))
        return f(*args, **kwargs)
    return decorated_function

# Diccionario con las secciones y sus clases
secciones = {
    "Doctrinas": [
        {"titulo": "Clase 1: La Revelación de Dios", "slug": "revelacion-de-dios", "video_url": "https://www.youtube.com/embed/MDlvQqrYSvs"},
        {"titulo": "Clase 2: La Imagen de Dios", "slug": "imagen-de-dios", "video_url": "https://www.youtube.com/embed/c2pA4-G2z_o"}
    ],
    "Carácter": [
        {"titulo": "Clase 1: El fruto del Espíritu", "slug": "fruto-del-espiritu", "video_url": "https://www.youtube.com/embed/qwerty5678"},
        {"titulo": "Clase 2: Humildad en acción", "slug": "humildad", "video_url": "https://www.youtube.com/embed/qazwsx1234"}
    ],
    "Oración": [
        {"titulo": "Clase 1: Cómo oraba Jesús", "slug": "como-oraba-jesus", "video_url": "https://www.youtube.com/embed/oracion1"},
        {"titulo": "Clase 2: Intercesión efectiva", "slug": "intercesion-efectiva", "video_url": "https://www.youtube.com/embed/oracion2"}
    ],
    "Sanidad Interior": [
        {"titulo": "Clase 1: Sanando el corazón herido", "slug": "sanando-corazon-herido", "video_url": "https://www.youtube.com/embed/sanidad1"},
        {"titulo": "Clase 2: Liberación emocional", "slug": "liberacion-emocional", "video_url": "https://www.youtube.com/embed/sanidad2"}
    ],
    "Carácter de Dios": [
        {"titulo": "Clase 1: Dios es amor", "slug": "dios-es-amor", "video_url": "https://www.youtube.com/embed/diosesamor1"},
        {"titulo": "Clase 2: Dios es justo", "slug": "dios-es-justo", "video_url": "https://www.youtube.com/embed/diosesjusto2"}
    ],
    "Palabra de Dios": [
        {"titulo": "Clase 1: La Biblia: Inspirada por Dios", "slug": "biblia-inspirada", "video_url": "https://www.youtube.com/embed/palabradedios1"},
        {"titulo": "Clase 2: Cómo estudiar la Escritura", "slug": "como-estudiar-escritura", "video_url": "https://www.youtube.com/embed/palabradedios2"},
        {"titulo": "Clase 3: La autoridad de la Palabra", "slug": "autoridad-palabra", "video_url": "https://www.youtube.com/embed/palabradedios3"}
    ]
}

@app.route('/')
def home():
    usuario_logueado = None
    if 'usuario_id' in session:
        # Obtener todos los datos del usuario desde la base de datos
        usuario_db = Usuario.query.get(session.get('usuario_id'))
        if usuario_db:
            usuario_logueado = {
                'nombre': usuario_db.nombre,
                'apellidos': usuario_db.apellidos,
                'email': usuario_db.email,
                'tipo_documento': usuario_db.tipo_documento,
                'numero_documento': usuario_db.numero_documento,
                'fecha_nacimiento': usuario_db.fecha_nacimiento,
                'telefono': usuario_db.telefono,
                'ciudad': usuario_db.ciudad,
                'pais': usuario_db.pais,
                'es_admin': usuario_db.es_admin
            }
    return render_template('index.html', secciones=secciones, usuario=usuario_logueado)

@app.route('/clase/<slug>')
@login_required
def clase(slug):
    for curso_slug, clases in secciones.items():
        for clase in clases:
            if clase["slug"] == slug:
                usuario_logueado = {
                    'nombre': session.get('usuario_nombre'),
                    'email': session.get('usuario_email')
                }
                return render_template('clase.html', clase=clase, curso_slug=curso_slug, usuario=usuario_logueado)
    return "Clase no encontrada", 404

# Ruta para registro de usuarios
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        contraseña = request.form['contraseña']

        existente = Usuario.query.filter_by(email=email).first()
        if existente:
            flash('⚠️ El correo ya está registrado.')
            return redirect(url_for('registro'))

        nuevo_usuario = Usuario(nombre=nombre, email=email)
        nuevo_usuario.set_password(contraseña)

        db.session.add(nuevo_usuario)
        db.session.commit()

        flash('✅ Registro exitoso. ¡Ya puedes iniciar sesión!')
        return redirect(url_for('home'))

    return render_template('registro.html')
@app.route('/login', methods=['GET'])
def login_form():
    return render_template('login.html')

# Ruta para procesar el formulario (POST)
@app.route('/login', methods=['POST'])
def login_post():
    email = request.form['email']
    contraseña = request.form['contraseña']

    usuario = Usuario.query.filter_by(email=email).first()
    if usuario and usuario.check_password(contraseña):
        session['usuario_id'] = usuario.id
        session['usuario_nombre'] = usuario.nombre
        session['usuario_email'] = usuario.email
        session['es_admin'] = usuario.es_admin
        flash('✅ Sesión iniciada con éxito')
        return redirect(url_for('home'))
    else:
        flash('❌ Credenciales incorrectas')
        return redirect(url_for('login_form'))

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.clear()
    flash('✅ Has cerrado sesión correctamente.')
    return redirect(url_for('home'))

# Ruta para el perfil del usuario (página separada)
@app.route('/perfil', methods=['GET', 'POST'])
@login_required
def perfil():
    usuario = Usuario.query.get(session['usuario_id'])
    
    if request.method == 'POST':
        # Actualizar datos del perfil
        usuario.nombre = request.form.get('nombre')
        usuario.apellidos = request.form.get('apellidos')
        usuario.tipo_documento = request.form.get('tipo_documento')
        usuario.numero_documento = request.form.get('numero_documento')
        usuario.telefono = request.form.get('telefono')
        usuario.ciudad = request.form.get('ciudad')
        usuario.pais = request.form.get('pais')
        
        # Procesar fecha de nacimiento
        fecha_nac = request.form.get('fecha_nacimiento')
        if fecha_nac:
            from datetime import datetime
            usuario.fecha_nacimiento = datetime.strptime(fecha_nac, '%Y-%m-%d').date()
        
        db.session.commit()
        
        # Actualizar el nombre en la sesión
        session['usuario_nombre'] = usuario.nombre
        
        # Si es petición AJAX, devolver JSON
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return {'success': True, 'message': 'Perfil actualizado exitosamente'}
        
        flash('✅ Perfil actualizado exitosamente.')
        return redirect(url_for('perfil'))
    
    return render_template('perfil.html', usuario=usuario)

# Ruta API para actualizar perfil desde la sección (AJAX)
@app.route('/api/actualizar-perfil', methods=['POST'])
@login_required
def api_actualizar_perfil():
    try:
        usuario = Usuario.query.get(session['usuario_id'])
        
        # Actualizar datos del perfil
        usuario.nombre = request.form.get('nombre')
        usuario.apellidos = request.form.get('apellidos')
        usuario.tipo_documento = request.form.get('tipo_documento')
        usuario.numero_documento = request.form.get('numero_documento')
        usuario.telefono = request.form.get('telefono')
        usuario.ciudad = request.form.get('ciudad')
        usuario.pais = request.form.get('pais')
        
        # Procesar fecha de nacimiento
        fecha_nac = request.form.get('fecha_nacimiento')
        if fecha_nac:
            from datetime import datetime
            usuario.fecha_nacimiento = datetime.strptime(fecha_nac, '%Y-%m-%d').date()
        
        db.session.commit()
        
        # Actualizar el nombre en la sesión
        session['usuario_nombre'] = usuario.nombre
        
        return {'success': True, 'message': 'Perfil actualizado exitosamente', 'nombre': usuario.nombre}
    except Exception as e:
        return {'success': False, 'message': f'Error: {str(e)}'}, 400

# Crear la base de datos si no existe
with app.app_context():
    db.create_all()
    print("✅ Base de datos inicializada correctamente")
@app.route('/restablecer', methods=['GET', 'POST'])
def restablecer():
    if request.method == 'POST':
        email = request.form['email']
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario:
            token = '123456'  # Aquí puedes generar un token real si quieres
            msg = Message('Instrucciones para restablecer tu contraseña',
                          sender='tucorreo@gmail.com',
                          recipients=[email])
            enlace_cambio = url_for('cambiar_contraseña', token=usuario.id, _external=True)
            msg.body = f"""Hola {usuario.nombre},

            Recibiste este correo porque solicitaste restablecer tu contraseña.

            Haz clic en el siguiente enlace para cambiar tu contraseña:
            {enlace_cambio}
            Si no solicitaste este cambio, ignora este correo.

            Bendiciones,
            El equipo de Berakah Emeth
            """
            mail.send(msg)
            flash('✅ Te hemos enviado instrucciones a tu correo.')
        else:
            flash('❌ Este correo no está registrado.')
        return redirect(url_for('login_form'))
    return render_template('restablecer.html')

@app.route('/cambiar-contraseña', methods=['GET', 'POST'])
def cambiar_contraseña():
    token = request.args.get('token')
    usuario = Usuario.query.filter_by(id=token).first()

    if not usuario:
        flash('❌ Token inválido.')
        return redirect(url_for('login_form'))

    if request.method == 'POST':
        nueva_contraseña = request.form['nueva_contraseña']
        usuario.set_password(nueva_contraseña)
        db.session.commit()
        flash('✅ Tu contraseña ha sido actualizada.')
        return redirect(url_for('login_form'))

    return render_template('cambiar_contraseña.html', usuario=usuario)

# API para marcar clase como completada
@app.route('/api/completar-clase', methods=['POST'])
@login_required
def completar_clase():
    data = request.get_json()
    curso_slug = data.get('curso_slug')
    clase_slug = data.get('clase_slug')
    
    if not curso_slug or not clase_slug:
        return jsonify({'success': False, 'message': 'Datos incompletos'}), 400
    
    usuario_id = session.get('usuario_id')
    
    # Verificar si ya está completada
    clase_existente = ClaseCompletada.query.filter_by(
        usuario_id=usuario_id,
        curso_slug=curso_slug,
        clase_slug=clase_slug
    ).first()
    
    if clase_existente:
        return jsonify({'success': True, 'message': 'Clase ya estaba completada', 'ya_completada': True})
    
    # Crear nuevo registro
    nueva_clase = ClaseCompletada(
        usuario_id=usuario_id,
        curso_slug=curso_slug,
        clase_slug=clase_slug
    )
    db.session.add(nueva_clase)
    db.session.commit()
    
    # Calcular progreso
    total_clases = len(secciones.get(curso_slug, []))
    clases_completadas = ClaseCompletada.query.filter_by(
        usuario_id=usuario_id,
        curso_slug=curso_slug
    ).count()
    
    porcentaje = int((clases_completadas / total_clases * 100)) if total_clases > 0 else 0
    
    return jsonify({
        'success': True,
        'message': '✅ Clase completada',
        'clases_completadas': clases_completadas,
        'total_clases': total_clases,
        'porcentaje': porcentaje
    })

# API para obtener progreso de un curso
@app.route('/api/progreso/<curso_slug>', methods=['GET'])
@login_required
def obtener_progreso(curso_slug):
    usuario_id = session.get('usuario_id')
    
    # Obtener clases completadas de este curso
    clases_completadas = ClaseCompletada.query.filter_by(
        usuario_id=usuario_id,
        curso_slug=curso_slug
    ).all()
    
    clases_slugs_completadas = [c.clase_slug for c in clases_completadas]
    
    # Calcular progreso
    total_clases = len(secciones.get(curso_slug, []))
    num_completadas = len(clases_completadas)
    porcentaje = int((num_completadas / total_clases * 100)) if total_clases > 0 else 0
    
    return jsonify({
        'success': True,
        'clases_completadas': clases_slugs_completadas,
        'num_completadas': num_completadas,
        'total_clases': total_clases,
        'porcentaje': porcentaje
    })

# API para obtener todo el progreso del usuario
@app.route('/api/progreso-general', methods=['GET'])
@login_required
def obtener_progreso_general():
    usuario_id = session.get('usuario_id')
    
    progreso_cursos = {}
    
    for curso_slug, clases in secciones.items():
        clases_completadas = ClaseCompletada.query.filter_by(
            usuario_id=usuario_id,
            curso_slug=curso_slug
        ).count()
        
        total_clases = len(clases)
        porcentaje = int((clases_completadas / total_clases * 100)) if total_clases > 0 else 0
        
        progreso_cursos[curso_slug] = {
            'completadas': clases_completadas,
            'total': total_clases,
            'porcentaje': porcentaje
        }
    
    return jsonify({
        'success': True,
        'progreso': progreso_cursos
    })

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # Modo debug activado para desarrollo ágil y profesional
    app.run(host='0.0.0.0', port=port, debug=True)



    



