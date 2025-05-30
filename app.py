from flask_sqlalchemy import SQLAlchemy
from models import db, Usuario
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:uoLTdxMcdpriiVvMsplZQDpWdEUIrVTB@postgres.railway.internal:5432/railway'
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
    ]
}

@app.route('/')
def home():
    return render_template('index.html', secciones=secciones)

@app.route('/clase/<slug>')
def clase(slug):
    for clases in secciones.values():
        for clase in clases:
            if clase["slug"] == slug:
                return render_template('clase.html', clase=clase)
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
        session['es_admin'] = usuario.es_admin
        flash('✅ Sesión iniciada con éxito')
        return redirect(url_for('home'))
    else:
        flash('❌ Credenciales incorrectas')
        return redirect(url_for('login_form'))

# Crear la base de datos si no existe
with app.app_context():
    db.create_all()
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
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)



    



