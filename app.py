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
    "Doctrina de Dios (Teología Propia)": [
        {
            "titulo": "Clase 1: Revelación general y especial", 
            "slug": "revelacion-general-especial", 
            "video_url": "https://www.youtube.com/embed/MDlvQqrYSvs", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 1: LA REVELACIÓN DE DIOS</h2>

<h3 style="color: #764ba2; margin-top: 25px;">¿Dios es un Relojero?</h3>
<p>En el vasto campo del pensamiento humano, una de las preguntas más profundas es si Dios se relaciona con la humanidad. Algunos sostienen que Dios, aunque real, permanece distante, mientras que otros creen que Él se ha revelado activamente a través de la creación y la historia. Este capítulo explora la doctrina de la revelación de Dios, abordando cómo Él se manifiesta al hombre, contrastando esta verdad bíblica con la perspectiva de los deístas, y reflexionando sobre nuestro papel en Su revelación.</p>

<p>Vamos a profundizar en la doctrina de la revelación a través de los siguientes pensamientos que se han dado al pasar de tiempo.</p>

<h4 style="color: #555; margin-top: 20px;">Dios no se revela al hombre</h4>
<p>Quienes afirman que Dios no se revela plantean dos razones principales. La primera es que <strong>Dios no existe</strong>, lo que implica que no hay nada que revelar ni un ser que lo haga. La inexistencia de Dios, por lo tanto, sería una negación total de cualquier comunicación divina. La segunda razón es que, aunque aceptan la existencia de Dios, argumentan que <strong>Él no tiene interés en relacionarse con Su creación</strong>, dejando al hombre en un vacío espiritual y existencial, ya que es un ser que crea por el simple hecho de que puede, sin ningún propósito o motivación específica, un Ser que no tiene nada en común con su creación.</p>

<div style="text-align: center; margin: 30px 0;">
<img src="/static/images/mapa-dios-no-se-revela.png" alt="Mapa mental - Dios no se revela" style="max-width: 100%; height: auto; border: 2px solid #ddd; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
<p style="font-size: 14px; color: #666; margin-top: 10px; font-style: italic;">Mapa mental: Posturas sobre la revelación de Dios</p>
</div>

<p>Estas dos posturas relacionadas a la revelación divina: el <strong>ateísmo</strong> y el <strong>deísmo</strong> se entienden como: el ateísmo defiende la idea de que Dios no existe, mientras que el deísmo, aunque reconoce la existencia de un Dios, niega su involucramiento activo con la creación. A este Dios se le ha denominado en diversos textos sobre el tema como el <strong>"Dios relojero"</strong>, haciendo referencia a la idea de un relojero que, al crear un reloj, se aleja de él una vez lo ha vendido, aunque es su creador. Según esta perspectiva, Dios construyó el universo, estableció sus leyes naturales y luego lo dejó funcionar de manera independiente, sin intervenir jamás.</p>

<h4 style="color: #555; margin-top: 20px;">Dos exponentes destacados del deísmo:</h4>

<p><strong>Salvador Freixedo:</strong> Este exsacerdote afirmaba: <em>"Mi Dios no es un Dios personal, no está acá, no se enfada, no perdona, no es hombre ni persona. Ese Dios es una amenaza para la humanidad y es un insulto para la inteligencia humana"</em>. Freixedo abandonó su fe en el Dios de la Biblia y dedicó su vida al estudio de la ufología, alejándose de la idea de un Dios personal y cercano al ser humano.</p>

<p><strong>Thomas Paine:</strong> Crítico de la religión organizada, Paine sostenía: <em>"Dios puede ser contemplado en la creación, no es necesario buscarlo en las escrituras"</em>. Paine fue aún más radical, llegando a calificar ciertos pasajes de la Biblia como obra de un "demonio usurpando el lugar de Dios", específicamente los que mostraban a Dios justo y que estaba cerca de su creación.</p>

<p>Para estos exponentes Dios era "Un relojero" creador que no se preocupa por su creación. <strong>Gracias a Dios tenemos el estudio de la revelación general y específica de Dios.</strong></p>

<h3 style="color: #764ba2; margin-top: 25px;">La Biblia nos enseña que Dios sí se revela al hombre</h3>
<p>A diferencia de otras creencias, la Biblia afirma que Dios no solo es real, sino que también busca tener una relación cercana y profunda con la humanidad y contigo personalmente. Esto lo vemos claramente en las Escrituras, donde se muestra a un Dios que, lejos de ser distante, se da a conocer de manera clara y directa a través de distintos medios. La visión bíblica contradice directamente al deísmo, presentando a un Dios que desea ser conocido y que se revela activamente al hombre.</p>

<p>Veamos que dice la Biblia. Según las Escrituras, esta revelación divina se manifiesta de dos formas principales:</p>

<h4 style="color: #667eea; margin-top: 20px;">� Revelación General</h4>
<p>La revelación general es la manifestación de Dios ya establecida a toda la humanidad a través de medios accesibles, como la creación, la mente y el corazón humano.</p>

<h5>• A través de la creación:</h5>
<p style="padding: 10px; background: #f0f4ff; border-left: 3px solid #667eea; margin: 10px 0;"><strong>Romanos 1:20</strong> - <em>"Porque desde la creación del mundo las cualidades invisibles de Dios, es decir, su eterno poder y su naturaleza divina, se perciben claramente a través de lo que él creó, de modo que nadie tiene excusa."</em></p>

<p>La palabra <strong>percibe claramente</strong> (<em>ἐφανερώθη - epanerōthē</em>), que aparece en Romanos 1:20 en el griego original, se traduce generalmente como "se ha manifestado" o "ha sido revelado". Esta palabra subraya la idea de que Dios se ha hecho visible o evidente de manera clara y comprensible. Esta forma verbal expresa que lo que antes estaba oculto o no era fácilmente accesible ahora se ha hecho claro y evidente para todos, sin dejar lugar a dudas. Dios se ha manifestado claramente a través de la creación, y esa manifestación es evidente para todos, como si fuera algo que se muestra abiertamente, sin esconderse.</p>

<h5>• En la mente y el corazón humano:</h5>
<p style="padding: 10px; background: #f0f4ff; border-left: 3px solid #667eea; margin: 10px 0;"><strong>Romanos 2:15</strong> - <em>"Estos muestran que llevan escrito en el corazón lo que la Ley exige, como lo atestigua su conciencia, pues sus propios pensamientos algunas veces los acusan y otras veces los excusan."</em></p>

<h4 style="color: #667eea; margin-top: 20px;">✝️ Revelación Específica</h4>
<p>La revelación específica es el acto de Dios manifestándose de manera directa y personal a individuos o grupos en momentos claves. Dios busca que le conozcamos íntimamente y entendamos Su voluntad para nuestras vidas. La mayor expresión de este amor fue el envío de Su único Hijo, Jesús, quien vino a este mundo para mostrar en plenitud el carácter y el propósito de Dios. En Jesús, Dios nos reveló Su amor incondicional y Su plan de salvación para toda la humanidad. <strong>No hay mayor revelación que esta.</strong></p>

<p>La revelación específica de Dios se manifiesta de diversas maneras, como en su llamado individual a Abraham para establecer un pacto (Génesis 12:1-9) y en la entrega de los Diez Mandamientos al pueblo de Israel mediante Moisés (Éxodo 20). Sin embargo, <strong>la mayor revelación de Dios es Jesucristo</strong>, quien, según Hebreos 1:1-4, es el reflejo perfecto de su gloria y esencia.</p>

<h4 style="color: #667eea; margin-top: 20px;">📚 La Fuente Suprema de Revelación: La Biblia</h4>
<p>La Biblia se presenta como la expresión más completa y suprema de la revelación divina. Inspirada por Dios, contiene todo lo necesario para que el hombre conozca a su Creador y viva de acuerdo con Su voluntad (2 Timoteo 3:16-17). En la Biblia encontramos no solo las palabras de Dios, sino también Su plan eterno para la redención de la humanidad, el propósito de la creación y el modelo para una vida plena en comunión con Él.</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p><strong>¿Es Dios un relojero que abandona Su obra después de crearla?</strong> La respuesta bíblica es un rotundo <strong>no</strong>. El Dios de la Biblia no es un observador distante, sino un Creador activo, que se involucra constantemente con Su creación.</p>

<div style="margin-top: 20px; padding: 20px; background: #eef5ff; border-left: 5px solid #667eea; border-radius: 8px;">
<p style="margin: 0;"><strong>Nuestro papel en esta revelación es doble:</strong></p>
<ol style="margin-top: 10px;">
<li><strong>Buscar activamente a Jesús</strong>, quien es la manifestación suprema de Dios.</li>
<li><strong>Estudiar la Biblia</strong>, permitiendo que transforme nuestra vida y nos capacite para compartir la verdad de Dios con los demás.</li>
</ol>
</div>
""", 
            "pdf_url": "/static/pdfs/revelacion-general-especial.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-revelacion-general-especial.pdf"
        }
    ],
    "Doctrina de la Revelación": [],
    "Doctrina de la Creación": [],
    "Doctrina del Hombre (Antropología)": [],
    "Doctrina del Pecado (Hamartiología)": [],
    "Doctrina de Cristo (Cristología)": [],
    "Doctrina del Espíritu Santo (Neumatología)": [],
    "Doctrina de la Salvación (Soteriología)": [],
    "Doctrina de la Iglesia (Eclesiología)": [],
    "Doctrina de los Últimos Tiempos (Escatología)": [],
    "Doctrina de la Ética Cristiana": [],
    "Doctrinas Especiales": [],
    "Carácter de Dios": [],
    "Carácter de Jesús": [],
    "Carácter del Espíritu Santo": [],
    "Palabra de Dios": [],
    "Disciplinas": [],
    "Oración": [
        {"titulo": "Clase 1: Cómo oraba Jesús", "slug": "como-oraba-jesus", "video_url": "https://www.youtube.com/embed/oracion1"},
        {"titulo": "Clase 2: Intercesión efectiva", "slug": "intercesion-efectiva", "video_url": "https://www.youtube.com/embed/oracion2"}
    ],
    "Sanidad Interior": [
        {"titulo": "Clase 1: Sanando el corazón herido", "slug": "sanando-corazon-herido", "video_url": "https://www.youtube.com/embed/sanidad1"},
        {"titulo": "Clase 2: Liberación emocional", "slug": "liberacion-emocional", "video_url": "https://www.youtube.com/embed/sanidad2"}
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



    



