from flask_sqlalchemy import SQLAlchemy
from models import db, Usuario, ClaseCompletada
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_mail import Mail, Message
from functools import wraps

app = Flask(__name__)
# Usar SQLite para desarrollo local, PostgreSQL para producción
import os
if os.environ.get('DATABASE_URL'):
    # Render y otras plataformas usan DATABASE_URL
    database_url = os.environ.get('DATABASE_URL')
    # Render usa postgresql://, pero SQLAlchemy necesita postgresql://
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
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
    "Doctrina de la Revelación Bíblica": [
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
        },
        {
            "titulo": "Clase 2: Inspiración bíblica",
            "slug": "inspiracion-biblica",
            "video_url": "",
            "descripcion": "<p>[Contenido pendiente]</p>",
            "pdf_url": "/static/pdfs/inspiracion-biblica.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-inspiracion-biblica.pdf"
        },
        {
            "titulo": "Clase 3: Inerrancia",
            "slug": "inerrancia",
            "video_url": "",
            "descripcion": "<p>[Contenido pendiente]</p>",
            "pdf_url": "/static/pdfs/inerrancia.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-inerrancia.pdf"
        },
        {
            "titulo": "Clase 4: Infalibilidad",
            "slug": "infalibilidad",
            "video_url": "",
            "descripcion": "<p>[Contenido pendiente]</p>",
            "pdf_url": "/static/pdfs/infalibilidad.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-infalibilidad.pdf"
        },
        {
            "titulo": "Clase 5: Canon de la Escritura",
            "slug": "canon-escritura",
            "video_url": "",
            "descripcion": "<p>[Contenido pendiente]</p>",
            "pdf_url": "/static/pdfs/canon-escritura.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-canon-escritura.pdf"
        },
        {
            "titulo": "Clase 6: Iluminación",
            "slug": "iluminacion",
            "video_url": "",
            "descripcion": "<p>[Contenido pendiente]</p>",
            "pdf_url": "/static/pdfs/iluminacion.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-iluminacion.pdf"
        },
        {
            "titulo": "Clase 7: Autoridad y suficiencia de la Biblia",
            "slug": "autoridad-suficiencia-biblia",
            "video_url": "",
            "descripcion": "<p>[Contenido pendiente]</p>",
            "pdf_url": "/static/pdfs/autoridad-suficiencia-biblia.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-autoridad-suficiencia-biblia.pdf"
        },
        {
            "titulo": "Clase 8: Hermenéutica bíblica",
            "slug": "hermeneutica-biblica",
            "video_url": "",
            "descripcion": "<p>[Contenido pendiente]</p>",
            "pdf_url": "/static/pdfs/hermeneutica-biblica.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-hermeneutica-biblica.pdf"
        }
    ],
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

<h4 style="color: #667eea; margin-top: 20px;">🌍 Revelación General</h4>
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
        },
        {
            "titulo": "Clase 2: Existencia de Dios", 
            "slug": "existencia-de-dios", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 2: LA EXISTENCIA DE DIOS</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/existencia-de-dios.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-existencia-de-dios.pdf"
        },
        {
            "titulo": "Clase 3: Atributos de Dios", 
            "slug": "atributos-de-dios", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 3: LOS ATRIBUTOS DE DIOS</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/atributos-de-dios.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-atributos-de-dios.pdf"
        },
        {
            "titulo": "Clase 4: La Trinidad", 
            "slug": "la-trinidad", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 4: LA TRINIDAD</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/la-trinidad.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-la-trinidad.pdf"
        }
    ],
    "Doctrina de la Creación": [
        {
            "titulo": "Clase 1: Acto creador", 
            "slug": "acto-creador", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 1: ACTO CREADOR</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/acto-creador.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-acto-creador.pdf"
        },
        {
            "titulo": "Clase 2: Ex nihilo", 
            "slug": "ex-nihilo", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 2: EX NIHILO (DE LA NADA)</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/ex-nihilo.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-ex-nihilo.pdf"
        },
        {
            "titulo": "Clase 3: Orden de la creación", 
            "slug": "orden-creacion", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 3: ORDEN DE LA CREACIÓN</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/orden-creacion.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-orden-creacion.pdf"
        },
        {
            "titulo": "Clase 4: Ángeles y seres espirituales", 
            "slug": "angeles-seres-espirituales", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 4: ÁNGELES Y SERES ESPIRITUALES</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/angeles-seres-espirituales.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-angeles-seres-espirituales.pdf"
        },
        {
            "titulo": "Clase 5: Mundo material", 
            "slug": "mundo-material", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 5: MUNDO MATERIAL</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/mundo-material.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-mundo-material.pdf"
        },
        {
            "titulo": "Clase 6: Mandato cultural", 
            "slug": "mandato-cultural", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 6: MANDATO CULTURAL</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/mandato-cultural.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-mandato-cultural.pdf"
        }
    ],
    "Doctrina del Hombre (Antropología)": [
        {
            "titulo": "Clase 1: Naturaleza del hombre", 
            "slug": "naturaleza-del-hombre", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 1: NATURALEZA DEL HOMBRE</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/naturaleza-del-hombre.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-naturaleza-del-hombre.pdf"
        },
        {
            "titulo": "Clase 2: Propósito del hombre", 
            "slug": "proposito-del-hombre", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 2: PROPÓSITO DEL HOMBRE</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/proposito-del-hombre.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-proposito-del-hombre.pdf"
        },
        {
            "titulo": "Clase 3: Responsabilidad moral", 
            "slug": "responsabilidad-moral", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 3: RESPONSABILIDAD MORAL</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/responsabilidad-moral.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-responsabilidad-moral.pdf"
        },
        {
            "titulo": "Clase 4: Libre albedrío vs voluntad caída", 
            "slug": "libre-albedrio-voluntad-caida", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 4: LIBRE ALBEDRÍO VS VOLUNTAD CAÍDA</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/libre-albedrio-voluntad-caida.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-libre-albedrio-voluntad-caida.pdf"
        },
        {
            "titulo": "Clase 5: La mujer en la creación", 
            "slug": "mujer-en-creacion", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 5: LA MUJER EN LA CREACIÓN</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/mujer-en-creacion.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-mujer-en-creacion.pdf"
        },
        {
            "titulo": "Clase 6: Matrimonio y familia", 
            "slug": "matrimonio-y-familia", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 6: MATRIMONIO Y FAMILIA</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/matrimonio-y-familia.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-matrimonio-y-familia.pdf"
        }
    ],
    "Doctrina del Pecado (Hamartiología)": [
        {
            "titulo": "Clase 1: Origen del pecado", 
            "slug": "origen-del-pecado", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 1: ORIGEN DEL PECADO</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/origen-del-pecado.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-origen-del-pecado.pdf"
        },
        {
            "titulo": "Clase 2: Caída de Adán", 
            "slug": "caida-de-adan", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 2: CAÍDA DE ADÁN</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/caida-de-adan.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-caida-de-adan.pdf"
        },
        {
            "titulo": "Clase 3: Naturaleza del pecado", 
            "slug": "naturaleza-del-pecado", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 3: NATURALEZA DEL PECADO</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/naturaleza-del-pecado.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-naturaleza-del-pecado.pdf"
        },
        {
            "titulo": "Clase 4: Total depravación", 
            "slug": "total-depravacion", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 4: TOTAL DEPRAVACIÓN</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/total-depravacion.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-total-depravacion.pdf"
        },
        {
            "titulo": "Clase 5: Pecado original", 
            "slug": "pecado-original", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 5: PECADO ORIGINAL</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/pecado-original.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-pecado-original.pdf"
        },
        {
            "titulo": "Clase 6: Pecados personales", 
            "slug": "pecados-personales", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 6: PECADOS PERSONALES</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/pecados-personales.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-pecados-personales.pdf"
        },
        {
            "titulo": "Clase 7: Pecado imperdonable", 
            "slug": "pecado-imperdonable", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 7: PECADO IMPERDONABLE</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/pecado-imperdonable.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-pecado-imperdonable.pdf"
        },
        {
            "titulo": "Clase 8: Consecuencias del pecado", 
            "slug": "consecuencias-del-pecado", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 8: CONSECUENCIAS DEL PECADO</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/consecuencias-del-pecado.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-consecuencias-del-pecado.pdf"
        }
    ],
    "Doctrina de Cristo (Cristología)": [
        {
            "titulo": "Clase 1: Preexistencia del Hijo", 
            "slug": "preexistencia-del-hijo", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 1: PREEXISTENCIA DEL HIJO</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/preexistencia-del-hijo.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-preexistencia-del-hijo.pdf"
        },
        {
            "titulo": "Clase 2: Encarnación", 
            "slug": "encarnacion", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 2: ENCARNACIÓN</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/encarnacion.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-encarnacion.pdf"
        },
        {
            "titulo": "Clase 3: Unión hipostática", 
            "slug": "union-hipostatica", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 3: UNIÓN HIPOSTÁTICA</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/union-hipostatica.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-union-hipostatica.pdf"
        },
        {
            "titulo": "Clase 4: Jesucristo verdadero Dios y verdadero hombre", 
            "slug": "jesucristo-dios-hombre", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 4: JESUCRISTO VERDADERO DIOS Y VERDADERO HOMBRE</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/jesucristo-dios-hombre.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-jesucristo-dios-hombre.pdf"
        },
        {
            "titulo": "Clase 5: Oficios de Cristo", 
            "slug": "oficios-de-cristo", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 5: OFICIOS DE CRISTO</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/oficios-de-cristo.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-oficios-de-cristo.pdf"
        },
        {
            "titulo": "Clase 6: Vida perfecta", 
            "slug": "vida-perfecta", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 6: VIDA PERFECTA</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/vida-perfecta.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-vida-perfecta.pdf"
        },
        {
            "titulo": "Clase 7: Muerte expiatoria", 
            "slug": "muerte-expiatoria", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 7: MUERTE EXPIATORIA</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/muerte-expiatoria.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-muerte-expiatoria.pdf"
        },
        {
            "titulo": "Clase 8: Sacrificio sustitutivo", 
            "slug": "sacrificio-sustitutivo", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 8: SACRIFICIO SUSTITUTIVO</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/sacrificio-sustitutivo.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-sacrificio-sustitutivo.pdf"
        },
        {
            "titulo": "Clase 9: Resurrección", 
            "slug": "resurreccion", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 9: RESURRECCIÓN</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/resurreccion.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-resurreccion.pdf"
        },
        {
            "titulo": "Clase 10: Ascensión", 
            "slug": "ascension", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 10: ASCENSIÓN</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/ascension.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-ascension.pdf"
        },
        {
            "titulo": "Clase 11: Intercesión presente", 
            "slug": "intercesion-presente", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 11: INTERCESIÓN PRESENTE</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/intercesion-presente.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-intercesion-presente.pdf"
        },
        {
            "titulo": "Clase 12: Segunda venida", 
            "slug": "segunda-venida", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 12: SEGUNDA VENIDA</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/segunda-venida.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-segunda-venida.pdf"
        }
    ],
    "Doctrina de la Salvación (Soteriología)": [
        {
            "titulo": "Clase 1: Llamamiento", 
            "slug": "llamamiento", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 1: LLAMAMIENTO</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/llamamiento.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-llamamiento.pdf"
        },
        {
            "titulo": "Clase 2: Regeneración", 
            "slug": "regeneracion", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 2: REGENERACIÓN</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/regeneracion.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-regeneracion.pdf"
        },
        {
            "titulo": "Clase 3: Conversión", 
            "slug": "conversion", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 3: CONVERSIÓN</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/conversion.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-conversion.pdf"
        },
        {
            "titulo": "Clase 4: Fe y arrepentimiento", 
            "slug": "fe-y-arrepentimiento", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 4: FE Y ARREPENTIMIENTO</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/fe-y-arrepentimiento.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-fe-y-arrepentimiento.pdf"
        },
        {
            "titulo": "Clase 5: Justificación", 
            "slug": "justificacion", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 5: JUSTIFICACIÓN</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/justificacion.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-justificacion.pdf"
        },
        {
            "titulo": "Clase 6: Adopción", 
            "slug": "adopcion", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 6: ADOPCIÓN</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/adopcion.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-adopcion.pdf"
        },
        {
            "titulo": "Clase 7: Unión con Cristo", 
            "slug": "union-con-cristo", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 7: UNIÓN CON CRISTO</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/union-con-cristo.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-union-con-cristo.pdf"
        },
        {
            "titulo": "Clase 8: Santificación", 
            "slug": "santificacion", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 8: SANTIFICACIÓN</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/santificacion.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-santificacion.pdf"
        },
        {
            "titulo": "Clase 9: Perseverancia", 
            "slug": "perseverancia", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 9: PERSEVERANCIA</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/perseverancia.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-perseverancia.pdf"
        },
        {
            "titulo": "Clase 10: Glorificación", 
            "slug": "glorificacion", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 10: GLORIFICACIÓN</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/glorificacion.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-glorificacion.pdf"
        },
        {
            "titulo": "Clase 11: Ordo Salutis", 
            "slug": "ordo-salutis", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 11: ORDO SALUTIS (ORDEN DE LA SALVACIÓN)</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/ordo-salutis.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-ordo-salutis.pdf"
        }
    ],
    "Doctrina del Espíritu Santo (Neumatología)": [
        {
            "titulo": "Clase 1: Personalidad y deidad del Espíritu", 
            "slug": "personalidad-deidad-espiritu", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 1: PERSONALIDAD Y DEIDAD DEL ESPÍRITU</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/personalidad-deidad-espiritu.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-personalidad-deidad-espiritu.pdf"
        },
        {
            "titulo": "Clase 2: Atributos del Espíritu y la Trinidad", 
            "slug": "atributos-espiritu-trinidad", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 2: ATRIBUTOS DEL ESPÍRITU Y LA TRINIDAD</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/atributos-espiritu-trinidad.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-atributos-espiritu-trinidad.pdf"
        },
        {
            "titulo": "Clase 3: Obra del Espíritu en AT", 
            "slug": "obra-espiritu-at", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 3: OBRA DEL ESPÍRITU EN EL ANTIGUO TESTAMENTO</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/obra-espiritu-at.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-obra-espiritu-at.pdf"
        },
        {
            "titulo": "Clase 4: Obra del Espíritu en Jesús", 
            "slug": "obra-espiritu-jesus", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 4: OBRA DEL ESPÍRITU EN JESÚS</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/obra-espiritu-jesus.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-obra-espiritu-jesus.pdf"
        },
        {
            "titulo": "Clase 5: Obra del Espíritu en el creyente", 
            "slug": "obra-espiritu-creyente", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 5: OBRA DEL ESPÍRITU EN EL CREYENTE</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/obra-espiritu-creyente.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-obra-espiritu-creyente.pdf"
        },
        {
            "titulo": "Clase 6: Regeneración por el Espíritu", 
            "slug": "regeneracion-espiritu", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 6: REGENERACIÓN POR EL ESPÍRITU</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/regeneracion-espiritu.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-regeneracion-espiritu.pdf"
        },
        {
            "titulo": "Clase 7: Conversión y el Espíritu", 
            "slug": "conversion-espiritu", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 7: CONVERSIÓN Y EL ESPÍRITU</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/conversion-espiritu.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-conversion-espiritu.pdf"
        },
        {
            "titulo": "Clase 8: Sellamiento del Espíritu", 
            "slug": "sellamiento-espiritu", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 8: SELLAMIENTO DEL ESPÍRITU</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/sellamiento-espiritu.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-sellamiento-espiritu.pdf"
        },
        {
            "titulo": "Clase 9: Bautismo en el Espíritu", 
            "slug": "bautismo-espiritu", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 9: BAUTISMO EN EL ESPÍRITU</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/bautismo-espiritu.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-bautismo-espiritu.pdf"
        },
        {
            "titulo": "Clase 10: Santificación por el Espíritu", 
            "slug": "santificacion-espiritu", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 10: SANTIFICACIÓN POR EL ESPÍRITU</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/santificacion-espiritu.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-santificacion-espiritu.pdf"
        },
        {
            "titulo": "Clase 11: Producción de frutos", 
            "slug": "produccion-frutos", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 11: PRODUCCIÓN DE FRUTOS</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/produccion-frutos.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-produccion-frutos.pdf"
        },
        {
            "titulo": "Clase 12: Convicción de pecado", 
            "slug": "conviccion-pecado", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 12: CONVICCIÓN DE PECADO</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/conviccion-pecado.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-conviccion-pecado.pdf"
        },
        {
            "titulo": "Clase 13: Obra del Espíritu en la Iglesia", 
            "slug": "obra-espiritu-iglesia", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 13: OBRA DEL ESPÍRITU EN LA IGLESIA</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/obra-espiritu-iglesia.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-obra-espiritu-iglesia.pdf"
        },
        {
            "titulo": "Clase 14: Dones espirituales", 
            "slug": "dones-espirituales", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 14: DONES ESPIRITUALES</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/dones-espirituales.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-dones-espirituales.pdf"
        },
        {
            "titulo": "Clase 15: Ministerio general del Espíritu", 
            "slug": "ministerio-general-espiritu", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 15: MINISTERIO GENERAL DEL ESPÍRITU</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/ministerio-general-espiritu.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-ministerio-general-espiritu.pdf"
        },
        {
            "titulo": "Clase 16: Blasfemia contra el Espíritu", 
            "slug": "blasfemia-espiritu", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 16: BLASFEMIA CONTRA EL ESPÍRITU</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/blasfemia-espiritu.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-blasfemia-espiritu.pdf"
        },
        {
            "titulo": "Clase 17: Escatología del Espíritu", 
            "slug": "escatologia-espiritu", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 17: ESCATOLOGÍA DEL ESPÍRITU</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/escatologia-espiritu.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-escatologia-espiritu.pdf"
        }
    ],
    "Doctrina de la Iglesia (Eclesiología)": [
        {
            "titulo": "Clase 1: Naturaleza de la Iglesia", 
            "slug": "naturaleza-de-la-iglesia", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 1: NATURALEZA DE LA IGLESIA</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/naturaleza-de-la-iglesia.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-naturaleza-de-la-iglesia.pdf"
        },
        {
            "titulo": "Clase 2: Ministerios en la Iglesia", 
            "slug": "ministerios-iglesia", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 2: MINISTERIOS EN LA IGLESIA</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/ministerios-iglesia.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-ministerios-iglesia.pdf"
        },
        {
            "titulo": "Clase 3: Sacramentos y Ordenanzas", 
            "slug": "sacramentos-ordenanzas", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 3: SACRAMENTOS Y ORDENANZAS</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/sacramentos-ordenanzas.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-sacramentos-ordenanzas.pdf"
        },
        {
            "titulo": "Clase 4: Adoración en la Iglesia", 
            "slug": "adoracion-iglesia", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 4: ADORACIÓN EN LA IGLESIA</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/adoracion-iglesia.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-adoracion-iglesia.pdf"
        },
        {
            "titulo": "Clase 5: Disciplina en la Iglesia", 
            "slug": "disciplina-iglesia", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 5: DISCIPLINA EN LA IGLESIA</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/disciplina-iglesia.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-disciplina-iglesia.pdf"
        },
        {
            "titulo": "Clase 6: Misión de la Iglesia", 
            "slug": "mision-iglesia", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 6: MISIÓN DE LA IGLESIA</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/mision-iglesia.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-mision-iglesia.pdf"
        },
        {
            "titulo": "Clase 7: Dones espirituales en el cuerpo", 
            "slug": "dones-espirituales-cuerpo", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 7: DONES ESPIRITUALES EN EL CUERPO</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/dones-espirituales-cuerpo.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-dones-espirituales-cuerpo.pdf"
        }
    ],
    "Doctrina de la Ética Cristiana": [
        {
            "titulo": "Clase 1: Ética bíblica", 
            "slug": "etica-biblica", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 1: ÉTICA BÍBLICA</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/etica-biblica.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-etica-biblica.pdf"
        },
        {
            "titulo": "Clase 2: Ley moral", 
            "slug": "ley-moral", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 2: LEY MORAL</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/ley-moral.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-ley-moral.pdf"
        },
        {
            "titulo": "Clase 3: Ética sexual", 
            "slug": "etica-sexual", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 3: ÉTICA SEXUAL</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/etica-sexual.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-etica-sexual.pdf"
        },
        {
            "titulo": "Clase 4: Ética familiar", 
            "slug": "etica-familiar", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 4: ÉTICA FAMILIAR</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/etica-familiar.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-etica-familiar.pdf"
        },
        {
            "titulo": "Clase 5: Ética laboral", 
            "slug": "etica-laboral", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 5: ÉTICA LABORAL</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/etica-laboral.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-etica-laboral.pdf"
        },
        {
            "titulo": "Clase 6: Ética social", 
            "slug": "etica-social", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 6: ÉTICA SOCIAL</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/etica-social.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-etica-social.pdf"
        },
        {
            "titulo": "Clase 7: Ética de la vida", 
            "slug": "etica-de-la-vida", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 7: ÉTICA DE LA VIDA</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/etica-de-la-vida.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-etica-de-la-vida.pdf"
        },
        {
            "titulo": "Clase 8: Ética en la política", 
            "slug": "etica-politica", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 8: ÉTICA EN LA POLÍTICA</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/etica-politica.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-etica-politica.pdf"
        },
        {
            "titulo": "Clase 9: Guerra, paz y violencia", 
            "slug": "guerra-paz-violencia", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 9: GUERRA, PAZ Y VIOLENCIA</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/guerra-paz-violencia.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-guerra-paz-violencia.pdf"
        }
    ],
    "Doctrina de los Últimos Tiempos (Escatología)": [
        {
            "titulo": "Clase 1: Estado intermedio", 
            "slug": "estado-intermedio", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 1: ESTADO INTERMEDIO</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/estado-intermedio.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-estado-intermedio.pdf"
        },
        {
            "titulo": "Clase 2: Segunda venida de Cristo", 
            "slug": "segunda-venida-cristo", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 2: SEGUNDA VENIDA DE CRISTO</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/segunda-venida-cristo.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-segunda-venida-cristo.pdf"
        },
        {
            "titulo": "Clase 3: Rapto", 
            "slug": "rapto", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 3: RAPTO</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/rapto.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-rapto.pdf"
        },
        {
            "titulo": "Clase 4: Gran tribulación", 
            "slug": "gran-tribulacion", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 4: GRAN TRIBULACIÓN</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/gran-tribulacion.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-gran-tribulacion.pdf"
        },
        {
            "titulo": "Clase 5: Milenio", 
            "slug": "milenio", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 5: MILENIO</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/milenio.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-milenio.pdf"
        },
        {
            "titulo": "Clase 6: Juicio final", 
            "slug": "juicio-final", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 6: JUICIO FINAL</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/juicio-final.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-juicio-final.pdf"
        },
        {
            "titulo": "Clase 7: Resurrección final", 
            "slug": "resurreccion-final", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 7: RESURRECCIÓN FINAL</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/resurreccion-final.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-resurreccion-final.pdf"
        },
        {
            "titulo": "Clase 8: Cielo", 
            "slug": "cielo", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 8: CIELO</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/cielo.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-cielo.pdf"
        },
        {
            "titulo": "Clase 9: Infierno", 
            "slug": "infierno", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 9: INFIERNO</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/infierno.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-infierno.pdf"
        },
        {
            "titulo": "Clase 10: Nueva creación", 
            "slug": "nueva-creacion", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 10: NUEVA CREACIÓN</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/nueva-creacion.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-nueva-creacion.pdf"
        }
    ],
    "Teología Comparada": [
        {
            "titulo": "Clase 1: Relaciones iglesia-estado", 
            "slug": "relaciones-iglesia-estado", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 1: RELACIONES IGLESIA-ESTADO</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/relaciones-iglesia-estado.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-relaciones-iglesia-estado.pdf"
        },
        {
            "titulo": "Clase 2: Demonología avanzada", 
            "slug": "demonologia-avanzada", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 2: DEMONOLOGÍA AVANZADA</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/demonologia-avanzada.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-demonologia-avanzada.pdf"
        },
        {
            "titulo": "Clase 3: Angelología", 
            "slug": "angelologia", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 3: ANGELOLOGÍA</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/angelologia.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-angelologia.pdf"
        },
        {
            "titulo": "Clase 4: Bautismo (debate teológico)", 
            "slug": "bautismo-debate", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 4: BAUTISMO (DEBATE TEOLÓGICO)</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/bautismo-debate.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-bautismo-debate.pdf"
        },
        {
            "titulo": "Clase 5: Rapto (posiciones teológicas)", 
            "slug": "rapto-posiciones", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 5: RAPTO (POSICIONES TEOLÓGICAS)</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/rapto-posiciones.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-rapto-posiciones.pdf"
        },
        {
            "titulo": "Clase 6: Don de lenguas", 
            "slug": "don-de-lenguas", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 6: DON DE LENGUAS</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/don-de-lenguas.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-don-de-lenguas.pdf"
        },
        {
            "titulo": "Clase 7: Predestinación", 
            "slug": "predestinacion", 
            "video_url": "", 
            "descripcion": """
<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">CAPÍTULO 7: PREDESTINACIÓN</h2>

<h3 style="color: #764ba2; margin-top: 25px;">Introducción</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Desarrollo</h3>
<p>[Contenido pendiente]</p>

<h3 style="color: #764ba2; margin-top: 25px;">Conclusión</h3>
<p>[Contenido pendiente]</p>
""", 
            "pdf_url": "/static/pdfs/predestinacion.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-predestinacion.pdf"
        }
    ],
    "Carácter de Dios": [
        {"titulo": "Clase 1: (Atributo Incomunicable) Aseidad", "slug": "aseidad", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/aseidad.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-aseidad.pdf"},
        {"titulo": "Clase 2: (Atributo Incomunicable) Simplicidad", "slug": "simplicidad", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/simplicidad.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-simplicidad.pdf"},
        {"titulo": "Clase 3: (Atributo Incomunicable) Inmutabilidad", "slug": "inmutabilidad", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/inmutabilidad.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-inmutabilidad.pdf"},
        {"titulo": "Clase 4: (Atributo Incomunicable) Eternidad", "slug": "eternidad-dios", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/eternidad-dios.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-eternidad-dios.pdf"},
        {"titulo": "Clase 5: (Atributo Incomunicable) Infinidad", "slug": "infinidad", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/infinidad.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-infinidad.pdf"},
        {"titulo": "Clase 6: (Atributo Incomunicable) Omnipresencia", "slug": "omnipresencia", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/omnipresencia.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-omnipresencia.pdf"},
        {"titulo": "Clase 7: (Atributo Incomunicable) Omnipotencia", "slug": "omnipotencia", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/omnipotencia.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-omnipotencia.pdf"},
        {"titulo": "Clase 8: (Atributo Incomunicable) Omnisciencia", "slug": "omnisciencia", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/omnisciencia.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-omnisciencia.pdf"},
        {"titulo": "Clase 9: (Atributo Incomunicable) Impasibilidad", "slug": "impasibilidad", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/impasibilidad.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-impasibilidad.pdf"},
        {"titulo": "Clase 10: (Atributo Incomunicable) Soberanía", "slug": "soberania", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/soberania.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-soberania.pdf"},
        {"titulo": "Clase 11: (Atributo Comunicable) Santidad", "slug": "santidad-dios", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/santidad-dios.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-santidad-dios.pdf"},
        {"titulo": "Clase 12: (Atributo Comunicable) Justicia", "slug": "justicia-dios", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/justicia-dios.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-justicia-dios.pdf"},
        {"titulo": "Clase 13: (Atributo Comunicable) Bondad", "slug": "bondad-dios", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/bondad-dios.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-bondad-dios.pdf"},
        {"titulo": "Clase 14: (Atributo Comunicable) Amor", "slug": "amor-dios", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/amor-dios.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-amor-dios.pdf"},
        {"titulo": "Clase 15: (Atributo Comunicable) Misericordia", "slug": "misericordia-dios", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/misericordia-dios.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-misericordia-dios.pdf"},
        {"titulo": "Clase 16: (Atributo Comunicable) Gracia", "slug": "gracia-dios", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/gracia-dios.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-gracia-dios.pdf"},
        {"titulo": "Clase 17: (Atributo Comunicable) Fidelidad", "slug": "fidelidad-dios", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/fidelidad-dios.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-fidelidad-dios.pdf"},
        {"titulo": "Clase 18: (Atributo Comunicable) Verdad", "slug": "verdad-dios", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/verdad-dios.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-verdad-dios.pdf"},
        {"titulo": "Clase 19: (Atributo Comunicable) Paciencia", "slug": "paciencia-dios", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/paciencia-dios.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-paciencia-dios.pdf"},
        {"titulo": "Clase 20: (Atributo Comunicable) Sabiduría", "slug": "sabiduria-dios", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/sabiduria-dios.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-sabiduria-dios.pdf"},
        {"titulo": "Clase 21: (Atributo Comunicable) Celos divinos", "slug": "celos-divinos", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/celos-divinos.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-celos-divinos.pdf"},
        {"titulo": "Clase 22: (Atributo Comunicable) Compasión", "slug": "compasion-dios", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/compasion-dios.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-compasion-dios.pdf"},
        {"titulo": "Clase 23: (Atributo Comunicable) Benignidad", "slug": "benignidad-dios", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/benignidad-dios.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-benignidad-dios.pdf"},
        {"titulo": "Clase 24: (Atributo Comunicable) Longanimidad", "slug": "longanimidad-dios", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/longanimidad-dios.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-longanimidad-dios.pdf"},
        {"titulo": "Clase 25: (Carácter) Dios perdona", "slug": "dios-perdona", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/dios-perdona.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-dios-perdona.pdf"},
        {"titulo": "Clase 26: (Carácter) Dios cumple promesas", "slug": "dios-cumple-promesas", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/dios-cumple-promesas.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-dios-cumple-promesas.pdf"},
        {"titulo": "Clase 27: (Carácter) Dios disciplina", "slug": "dios-disciplina", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/dios-disciplina.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-dios-disciplina.pdf"},
        {"titulo": "Clase 28: (Carácter) Dios provee", "slug": "dios-provee", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/dios-provee.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-dios-provee.pdf"},
        {"titulo": "Clase 29: (Carácter) Dios guía", "slug": "dios-guia", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/dios-guia.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-dios-guia.pdf"},
        {"titulo": "Clase 30: (Carácter) Dios protege", "slug": "dios-protege", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/dios-protege.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-dios-protege.pdf"},
        {"titulo": "Clase 31: (Carácter) Dios salva", "slug": "dios-salva", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/dios-salva.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-dios-salva.pdf"},
        {"titulo": "Clase 32: (Carácter) Dios consuela", "slug": "dios-consuela", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/dios-consuela.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-dios-consuela.pdf"},
        {"titulo": "Clase 33: (Carácter) Dios restaura", "slug": "dios-restaura", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/dios-restaura.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-dios-restaura.pdf"},
        {"titulo": "Clase 34: (Carácter) Dios cuida de Su pueblo", "slug": "dios-cuida-pueblo", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/dios-cuida-pueblo.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-dios-cuida-pueblo.pdf"},
        {"titulo": "Clase 35: (Carácter) Dios defiende la justicia", "slug": "dios-defiende-justicia", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/dios-defiende-justicia.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-dios-defiende-justicia.pdf"},
        {"titulo": "Clase 36: (Carácter) Dios escucha la oración", "slug": "dios-escucha-oracion", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/dios-escucha-oracion.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-dios-escucha-oracion.pdf"},
        {"titulo": "Clase 37: (Carácter) Dios se compadece del débil", "slug": "dios-compadece-debil", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/dios-compadece-debil.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-dios-compadece-debil.pdf"},
        {"titulo": "Clase 38: (Carácter) Dios libra al afligido", "slug": "dios-libra-afligido", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/dios-libra-afligido.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-dios-libra-afligido.pdf"},
        {"titulo": "Clase 39: (Carácter) Dios es cercano al quebrantado", "slug": "dios-cercano-quebrantado", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/dios-cercano-quebrantado.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-dios-cercano-quebrantado.pdf"},
        {"titulo": "Clase 40: (Carácter) Dios recompensa la obediencia", "slug": "dios-recompensa-obediencia", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/dios-recompensa-obediencia.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-dios-recompensa-obediencia.pdf"},
        {"titulo": "Clase 41: (Carácter) Dios transforma corazones", "slug": "dios-transforma-corazones", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/dios-transforma-corazones.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-dios-transforma-corazones.pdf"},
        {"titulo": "Clase 42: (Carácter) Dios está presente en el sufrimiento", "slug": "dios-presente-sufrimiento", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/dios-presente-sufrimiento.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-dios-presente-sufrimiento.pdf"}
    ],
    "Carácter de Jesús": [
        {"titulo": "Clase 1: (Atributo Incomunicable) Eternidad", "slug": "eternidad-jesus", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/eternidad-jesus.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-eternidad-jesus.pdf"},
        {"titulo": "Clase 2: (Atributo Incomunicable) Omnipotencia", "slug": "omnipotencia-jesus", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/omnipotencia-jesus.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-omnipotencia-jesus.pdf"},
        {"titulo": "Clase 3: (Atributo Incomunicable) Omnisciencia", "slug": "omnisciencia-jesus", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/omnisciencia-jesus.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-omnisciencia-jesus.pdf"},
        {"titulo": "Clase 4: (Atributo Incomunicable) Omnipresencia", "slug": "omnipresencia-jesus", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/omnipresencia-jesus.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-omnipresencia-jesus.pdf"},
        {"titulo": "Clase 5: (Atributo Incomunicable) Inmutabilidad", "slug": "inmutabilidad-jesus", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/inmutabilidad-jesus.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-inmutabilidad-jesus.pdf"},
        {"titulo": "Clase 6: (Atributo Incomunicable) Soberanía", "slug": "soberania-jesus", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/soberania-jesus.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-soberania-jesus.pdf"},
        {"titulo": "Clase 7: (Atributo Incomunicable) Santidad absoluta", "slug": "santidad-absoluta-jesus", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/santidad-absoluta-jesus.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-santidad-absoluta-jesus.pdf"},
        {"titulo": "Clase 8: (Atributo Incomunicable) Divinidad plena", "slug": "divinidad-plena-jesus", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/divinidad-plena-jesus.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-divinidad-plena-jesus.pdf"},
        {"titulo": "Clase 9: (Atributo Comunicable) Amor sacrificial", "slug": "amor-sacrificial-jesus", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/amor-sacrificial-jesus.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-amor-sacrificial-jesus.pdf"},
        {"titulo": "Clase 10: (Atributo Comunicable) Humildad", "slug": "humildad-jesus", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/humildad-jesus.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-humildad-jesus.pdf"},
        {"titulo": "Clase 11: (Atributo Comunicable) Mansedumbre", "slug": "mansedumbre-jesus", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/mansedumbre-jesus.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-mansedumbre-jesus.pdf"},
        {"titulo": "Clase 12: (Atributo Comunicable) Compasión", "slug": "compasion-jesus", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/compasion-jesus.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-compasion-jesus.pdf"},
        {"titulo": "Clase 13: (Atributo Comunicable) Bondad", "slug": "bondad-jesus", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/bondad-jesus.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-bondad-jesus.pdf"},
        {"titulo": "Clase 14: (Atributo Comunicable) Justicia", "slug": "justicia-jesus", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/justicia-jesus.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-justicia-jesus.pdf"},
        {"titulo": "Clase 15: (Atributo Comunicable) Verdad", "slug": "verdad-jesus", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/verdad-jesus.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-verdad-jesus.pdf"},
        {"titulo": "Clase 16: (Atributo Comunicable) Paciencia", "slug": "paciencia-jesus", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/paciencia-jesus.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-paciencia-jesus.pdf"},
        {"titulo": "Clase 17: (Atributo Comunicable) Obediencia perfecta al Padre", "slug": "obediencia-perfecta-jesus", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/obediencia-perfecta-jesus.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-obediencia-perfecta-jesus.pdf"},
        {"titulo": "Clase 18: (Atributo Comunicable) Fidelidad", "slug": "fidelidad-jesus", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/fidelidad-jesus.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-fidelidad-jesus.pdf"},
        {"titulo": "Clase 19: (Atributo Comunicable) Sabiduría divina", "slug": "sabiduria-divina-jesus", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/sabiduria-divina-jesus.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-sabiduria-divina-jesus.pdf"},
        {"titulo": "Clase 20: (Atributo Comunicable) Santidad práctica", "slug": "santidad-practica-jesus", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/santidad-practica-jesus.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-santidad-practica-jesus.pdf"},
        {"titulo": "Clase 21: (Atributo Comunicable) Celo santo por la casa de Dios", "slug": "celo-santo-jesus", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/celo-santo-jesus.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-celo-santo-jesus.pdf"},
        {"titulo": "Clase 22: (Carácter) Jesús perdona", "slug": "jesus-perdona", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/jesus-perdona.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-jesus-perdona.pdf"},
        {"titulo": "Clase 23: (Carácter) Jesús sana", "slug": "jesus-sana", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/jesus-sana.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-jesus-sana.pdf"},
        {"titulo": "Clase 24: (Carácter) Jesús restaura al caído", "slug": "jesus-restaura-caido", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/jesus-restaura-caido.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-jesus-restaura-caido.pdf"},
        {"titulo": "Clase 25: (Carácter) Jesús busca al perdido", "slug": "jesus-busca-perdido", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/jesus-busca-perdido.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-jesus-busca-perdido.pdf"},
        {"titulo": "Clase 26: (Carácter) Jesús no condena, pero llama al arrepentimiento", "slug": "jesus-no-condena", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/jesus-no-condena.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-jesus-no-condena.pdf"},
        {"titulo": "Clase 27: (Carácter) Jesús escucha y atiende al necesitado", "slug": "jesus-escucha-necesitado", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/jesus-escucha-necesitado.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-jesus-escucha-necesitado.pdf"},
        {"titulo": "Clase 28: (Carácter) Jesús confronta el pecado con verdad y amor", "slug": "jesus-confronta-pecado", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/jesus-confronta-pecado.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-jesus-confronta-pecado.pdf"},
        {"titulo": "Clase 29: (Carácter) Jesús sirve y se entrega por otros", "slug": "jesus-sirve-entrega", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/jesus-sirve-entrega.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-jesus-sirve-entrega.pdf"},
        {"titulo": "Clase 30: (Carácter) Jesús es amigo fiel", "slug": "jesus-amigo-fiel", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/jesus-amigo-fiel.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-jesus-amigo-fiel.pdf"},
        {"titulo": "Clase 31: (Carácter) Jesús protege y defiende a Su pueblo", "slug": "jesus-protege-defiende", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/jesus-protege-defiende.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-jesus-protege-defiende.pdf"},
        {"titulo": "Clase 32: (Carácter) Jesús tiene autoridad absoluta", "slug": "jesus-autoridad-absoluta", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/jesus-autoridad-absoluta.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-jesus-autoridad-absoluta.pdf"},
        {"titulo": "Clase 33: (Carácter) Jesús es misericordioso con los débiles", "slug": "jesus-misericordioso-debiles", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/jesus-misericordioso-debiles.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-jesus-misericordioso-debiles.pdf"},
        {"titulo": "Clase 34: (Carácter) Jesús se compadece del que sufre", "slug": "jesus-compadece-sufre", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/jesus-compadece-sufre.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-jesus-compadece-sufre.pdf"},
        {"titulo": "Clase 35: (Carácter) Jesús bendice y multiplica lo poco", "slug": "jesus-bendice-multiplica", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/jesus-bendice-multiplica.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-jesus-bendice-multiplica.pdf"},
        {"titulo": "Clase 36: (Carácter) Jesús trae paz en medio de la tormenta", "slug": "jesus-paz-tormenta", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/jesus-paz-tormenta.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-jesus-paz-tormenta.pdf"},
        {"titulo": "Clase 37: (Carácter) Jesús obedece hasta la muerte", "slug": "jesus-obedece-muerte", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/jesus-obedece-muerte.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-jesus-obedece-muerte.pdf"},
        {"titulo": "Clase 38: (Carácter) Jesús vence el mal con el bien", "slug": "jesus-vence-mal", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/jesus-vence-mal.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-jesus-vence-mal.pdf"},
        {"titulo": "Clase 39: (Carácter) Jesús transforma vidas", "slug": "jesus-transforma-vidas", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/jesus-transforma-vidas.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-jesus-transforma-vidas.pdf"},
        {"titulo": "Clase 40: (Carácter) Jesús es victorioso y triunfante", "slug": "jesus-victorioso-triunfante", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/jesus-victorioso-triunfante.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-jesus-victorioso-triunfante.pdf"}
    ],
    "Carácter del Espíritu Santo": [
        {"titulo": "Clase 1: (Atributo Incomunicable) Eternidad", "slug": "eternidad-espiritu", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/eternidad-espiritu.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-eternidad-espiritu.pdf"},
        {"titulo": "Clase 2: (Atributo Incomunicable) Omnipotencia", "slug": "omnipotencia-espiritu", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/omnipotencia-espiritu.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-omnipotencia-espiritu.pdf"},
        {"titulo": "Clase 3: (Atributo Incomunicable) Omnisciencia", "slug": "omnisciencia-espiritu", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/omnisciencia-espiritu.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-omnisciencia-espiritu.pdf"},
        {"titulo": "Clase 4: (Atributo Incomunicable) Omnipresencia", "slug": "omnipresencia-espiritu", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/omnipresencia-espiritu.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-omnipresencia-espiritu.pdf"},
        {"titulo": "Clase 5: (Atributo Incomunicable) Inmutabilidad", "slug": "inmutabilidad-espiritu", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/inmutabilidad-espiritu.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-inmutabilidad-espiritu.pdf"},
        {"titulo": "Clase 6: (Atributo Incomunicable) Santidad perfecta", "slug": "santidad-perfecta-espiritu", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/santidad-perfecta-espiritu.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-santidad-perfecta-espiritu.pdf"},
        {"titulo": "Clase 7: (Atributo Incomunicable) Soberanía", "slug": "soberania-espiritu", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/soberania-espiritu.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-soberania-espiritu.pdf"},
        {"titulo": "Clase 8: (Atributo Incomunicable) Divinidad plena", "slug": "divinidad-plena-espiritu", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/divinidad-plena-espiritu.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-divinidad-plena-espiritu.pdf"},
        {"titulo": "Clase 9: (Atributo Comunicable) Amor", "slug": "amor-espiritu", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/amor-espiritu.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-amor-espiritu.pdf"},
        {"titulo": "Clase 10: (Atributo Comunicable) Gozo", "slug": "gozo-espiritu", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/gozo-espiritu.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-gozo-espiritu.pdf"},
        {"titulo": "Clase 11: (Atributo Comunicable) Paz", "slug": "paz-espiritu", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/paz-espiritu.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-paz-espiritu.pdf"},
        {"titulo": "Clase 12: (Atributo Comunicable) Paciencia", "slug": "paciencia-espiritu", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/paciencia-espiritu.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-paciencia-espiritu.pdf"},
        {"titulo": "Clase 13: (Atributo Comunicable) Benignidad", "slug": "benignidad-espiritu", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/benignidad-espiritu.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-benignidad-espiritu.pdf"},
        {"titulo": "Clase 14: (Atributo Comunicable) Bondad", "slug": "bondad-espiritu", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/bondad-espiritu.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-bondad-espiritu.pdf"},
        {"titulo": "Clase 15: (Atributo Comunicable) Fe", "slug": "fe-espiritu", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/fe-espiritu.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-fe-espiritu.pdf"},
        {"titulo": "Clase 16: (Atributo Comunicable) Mansedumbre", "slug": "mansedumbre-espiritu", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/mansedumbre-espiritu.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-mansedumbre-espiritu.pdf"},
        {"titulo": "Clase 17: (Atributo Comunicable) Templanza", "slug": "templanza-espiritu", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/templanza-espiritu.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-templanza-espiritu.pdf"},
        {"titulo": "Clase 18: (Atributo Comunicable) Santificación", "slug": "santificacion-espiritu", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/santificacion-espiritu.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-santificacion-espiritu.pdf"},
        {"titulo": "Clase 19: (Atributo Comunicable) Sabiduría", "slug": "sabiduria-espiritu", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/sabiduria-espiritu.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-sabiduria-espiritu.pdf"},
        {"titulo": "Clase 20: (Atributo Comunicable) Consuelo", "slug": "consuelo-espiritu", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/consuelo-espiritu.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-consuelo-espiritu.pdf"},
        {"titulo": "Clase 21: (Carácter) El Espíritu Santo convence de pecado", "slug": "espiritu-convence-pecado", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/espiritu-convence-pecado.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-espiritu-convence-pecado.pdf"},
        {"titulo": "Clase 22: (Carácter) El Espíritu Santo regenera", "slug": "espiritu-regenera", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/espiritu-regenera.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-espiritu-regenera.pdf"},
        {"titulo": "Clase 23: (Carácter) El Espíritu Santo transforma vidas", "slug": "espiritu-transforma-vidas", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/espiritu-transforma-vidas.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-espiritu-transforma-vidas.pdf"},
        {"titulo": "Clase 24: (Carácter) El Espíritu Santo guía a toda verdad", "slug": "espiritu-guia-verdad", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/espiritu-guia-verdad.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-espiritu-guia-verdad.pdf"},
        {"titulo": "Clase 25: (Carácter) El Espíritu Santo enseña", "slug": "espiritu-ensena", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/espiritu-ensena.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-espiritu-ensena.pdf"},
        {"titulo": "Clase 26: (Carácter) El Espíritu Santo santifica", "slug": "espiritu-santifica", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/espiritu-santifica.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-espiritu-santifica.pdf"},
        {"titulo": "Clase 27: (Carácter) El Espíritu Santo da poder para testificar", "slug": "espiritu-poder-testificar", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/espiritu-poder-testificar.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-espiritu-poder-testificar.pdf"},
        {"titulo": "Clase 28: (Carácter) El Espíritu Santo consuela", "slug": "espiritu-consuela", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/espiritu-consuela.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-espiritu-consuela.pdf"},
        {"titulo": "Clase 29: (Carácter) El Espíritu Santo intercede por nosotros", "slug": "espiritu-intercede", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/espiritu-intercede.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-espiritu-intercede.pdf"},
        {"titulo": "Clase 30: (Carácter) El Espíritu Santo da dones para edificar", "slug": "espiritu-dones-edificar", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/espiritu-dones-edificar.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-espiritu-dones-edificar.pdf"},
        {"titulo": "Clase 31: (Carácter) El Espíritu Santo distribuye dones soberanamente", "slug": "espiritu-distribuye-dones", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/espiritu-distribuye-dones.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-espiritu-distribuye-dones.pdf"},
        {"titulo": "Clase 32: (Carácter) El Espíritu Santo produce unidad", "slug": "espiritu-produce-unidad", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/espiritu-produce-unidad.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-espiritu-produce-unidad.pdf"},
        {"titulo": "Clase 33: (Carácter) El Espíritu Santo glorifica a Cristo", "slug": "espiritu-glorifica-cristo", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/espiritu-glorifica-cristo.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-espiritu-glorifica-cristo.pdf"},
        {"titulo": "Clase 34: (Carácter) El Espíritu Santo revela la Palabra", "slug": "espiritu-revela-palabra", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/espiritu-revela-palabra.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-espiritu-revela-palabra.pdf"},
        {"titulo": "Clase 35: (Carácter) El Espíritu Santo capacita para el servicio", "slug": "espiritu-capacita-servicio", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/espiritu-capacita-servicio.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-espiritu-capacita-servicio.pdf"},
        {"titulo": "Clase 36: (Carácter) El Espíritu Santo libera cautivos", "slug": "espiritu-libera-cautivos", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/espiritu-libera-cautivos.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-espiritu-libera-cautivos.pdf"},
        {"titulo": "Clase 37: (Carácter) El Espíritu Santo purifica la iglesia", "slug": "espiritu-purifica-iglesia", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/espiritu-purifica-iglesia.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-espiritu-purifica-iglesia.pdf"},
        {"titulo": "Clase 38: (Carácter) El Espíritu Santo da vida espiritual", "slug": "espiritu-vida-espiritual", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/espiritu-vida-espiritual.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-espiritu-vida-espiritual.pdf"},
        {"titulo": "Clase 39: (Carácter) El Espíritu Santo preserva al creyente", "slug": "espiritu-preserva-creyente", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/espiritu-preserva-creyente.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-espiritu-preserva-creyente.pdf"},
        {"titulo": "Clase 40: (Carácter) El Espíritu Santo llena y controla", "slug": "espiritu-llena-controla", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/espiritu-llena-controla.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-espiritu-llena-controla.pdf"}
    ],
    "Disciplinas": [
        {
            "titulo": "Clase 1: Palabra (leer, meditar, obedecer)",
            "slug": "disciplina-palabra",
            "video_url": "",
            "descripcion": "<p>[Contenido pendiente]</p>",
            "pdf_url": "/static/pdfs/disciplina-palabra.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-disciplina-palabra.pdf"
        },
        {
            "titulo": "Clase 2: Oración",
            "slug": "disciplina-oracion",
            "video_url": "",
            "descripcion": "<p>[Contenido pendiente]</p>",
            "pdf_url": "/static/pdfs/disciplina-oracion.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-disciplina-oracion.pdf"
        },
        {
            "titulo": "Clase 3: Congregarse y comunión",
            "slug": "disciplina-congregarse",
            "video_url": "",
            "descripcion": "<p>[Contenido pendiente]</p>",
            "pdf_url": "/static/pdfs/disciplina-congregarse.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-disciplina-congregarse.pdf"
        },
        {
            "titulo": "Clase 4: Adoración",
            "slug": "disciplina-adoracion",
            "video_url": "",
            "descripcion": "<p>[Contenido pendiente]</p>",
            "pdf_url": "/static/pdfs/disciplina-adoracion.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-disciplina-adoracion.pdf"
        },
        {
            "titulo": "Clase 5: Ayuno",
            "slug": "disciplina-ayuno",
            "video_url": "",
            "descripcion": "<p>[Contenido pendiente]</p>",
            "pdf_url": "/static/pdfs/disciplina-ayuno.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-disciplina-ayuno.pdf"
        },
        {
            "titulo": "Clase 6: Confesión y arrepentimiento",
            "slug": "disciplina-confesion",
            "video_url": "",
            "descripcion": "<p>[Contenido pendiente]</p>",
            "pdf_url": "/static/pdfs/disciplina-confesion.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-disciplina-confesion.pdf"
        },
        {
            "titulo": "Clase 7: Servicio y evangelización",
            "slug": "disciplina-servicio",
            "video_url": "",
            "descripcion": "<p>[Contenido pendiente]</p>",
            "pdf_url": "/static/pdfs/disciplina-servicio.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-disciplina-servicio.pdf"
        },
        {
            "titulo": "Clase 8: Generosidad",
            "slug": "disciplina-generosidad",
            "video_url": "",
            "descripcion": "<p>[Contenido pendiente]</p>",
            "pdf_url": "/static/pdfs/disciplina-generosidad.pdf",
            "actividad_pdf_url": "/static/pdfs/respuestas-disciplina-generosidad.pdf"
        }
    ],
    "Sanidad Interior": [
        {"titulo": "Clase 1: Convicción del Espíritu Santo", "slug": "convencion-espiritu-santo", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/convencion-espiritu-santo.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-convencion-espiritu-santo.pdf"},
        {"titulo": "Clase 2: Arrepentimiento genuino", "slug": "arrepentimiento-genuino", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/arrepentimiento-genuino.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-arrepentimiento-genuino.pdf"},
        {"titulo": "Clase 3: Confesión y exposición del pecado", "slug": "confesion-exposicion-pecado", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/confesion-exposicion-pecado.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-confesion-exposicion-pecado.pdf"},
        {"titulo": "Clase 4: Recibir el perdón de Dios", "slug": "recibir-perdon-dios", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/recibir-perdon-dios.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-recibir-perdon-dios.pdf"},
        {"titulo": "Clase 5: Perdonar a otros", "slug": "perdonar-otros", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/perdonar-otros.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-perdonar-otros.pdf"},
        {"titulo": "Clase 6: Restauración de la identidad en Cristo", "slug": "restauracion-identidad-cristo", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/restauracion-identidad-cristo.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-restauracion-identidad-cristo.pdf"},
        {"titulo": "Clase 7: Renovación de la mente", "slug": "renovacion-mente", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/renovacion-mente.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-renovacion-mente.pdf"},
        {"titulo": "Clase 8: Liberación y rompimiento de ataduras", "slug": "liberacion-rompimiento-ataduras", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/liberacion-rompimiento-ataduras.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-liberacion-rompimiento-ataduras.pdf"},
        {"titulo": "Clase 9: Restauración relacional", "slug": "restauracion-relacional", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/restauracion-relacional.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-restauracion-relacional.pdf"},
        {"titulo": "Clase 10: Sanidad del corazón herido", "slug": "sanidad-corazon-herido", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/sanidad-corazon-herido.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-sanidad-corazon-herido.pdf"},
        {"titulo": "Clase 11: Santificación diaria", "slug": "santificacion-diaria", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/santificacion-diaria.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-santificacion-diaria.pdf"},
        {"titulo": "Clase 12: Restitución y frutos visibles", "slug": "restitucion-frutos-visibles", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/restitucion-frutos-visibles.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-restitucion-frutos-visibles.pdf"},
        {"titulo": "Clase 13: Propósito y misión", "slug": "proposito-mision", "video_url": "", "descripcion": "<p>[Contenido pendiente]</p>", "pdf_url": "/static/pdfs/proposito-mision.pdf", "actividad_pdf_url": "/static/pdfs/respuestas-proposito-mision.pdf"}
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

# Crear tablas automáticamente al iniciar
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # Modo debug activado para desarrollo ágil y profesional
    app.run(host='0.0.0.0', port=port, debug=True)



    



