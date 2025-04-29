from flask import Flask, render_template

app = Flask(__name__)

# Diccionario con las secciones y sus clases
secciones = {
    "Doctrinas": [
        {
            "titulo": "Clase 1: La Revelación de Dios",
            "slug": "revelacion-de-dios",
            "video_url": "https://www.youtube.com/embed/MDlvQqrYSvs"
        },
        {
            "titulo": "Clase 2: La Imagen de Dios",
            "slug": "imagen-de-dios",
            "video_url": "https://www.youtube.com/embed/c2pA4-G2z_o"
        }
    ],
    "Carácter": [
        {
            "titulo": "Clase 1: El fruto del Espíritu",
            "slug": "fruto-del-espiritu",
            "video_url": "https://www.youtube.com/embed/qwerty5678"
        },
        {
            "titulo": "Clase 2: Humildad en acción",
            "slug": "humildad",
            "video_url": "https://www.youtube.com/embed/qazwsx1234"
        }
    ],
    "Oración": [
        {
            "titulo": "Clase 1: Cómo oraba Jesús",
            "slug": "como-oraba-jesus",
            "video_url": "https://www.youtube.com/embed/oracion1"
        },
        {
            "titulo": "Clase 2: Intercesión efectiva",
            "slug": "intercesion-efectiva",
            "video_url": "https://www.youtube.com/embed/oracion2"
        }
    ],
    "Sanidad Interior": [
        {
            "titulo": "Clase 1: Sanando el corazón herido",
            "slug": "sanando-corazon-herido",
            "video_url": "https://www.youtube.com/embed/sanidad1"
        },
        {
            "titulo": "Clase 2: Liberación emocional",
            "slug": "liberacion-emocional",
            "video_url": "https://www.youtube.com/embed/sanidad2"
        }
    ],
    "Carácter de Dios": [
        {
            "titulo": "Clase 1: Dios es amor",
            "slug": "dios-es-amor",
            "video_url": "https://www.youtube.com/embed/diosesamor1"
        },
        {
            "titulo": "Clase 2: Dios es justo",
            "slug": "dios-es-justo",
            "video_url": "https://www.youtube.com/embed/diosesjusto2"
        }
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

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))  # 5000 es valor por defecto local
    app.run(host='0.0.0.0', port=port)

