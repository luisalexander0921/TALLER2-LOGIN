from flask import Flask
from controllers.animal_controller import animal_bp

app = Flask(__name__, template_folder='views')
app.secret_key = 'boa_constrictor'

# Registrar el blueprint de animales
app.register_blueprint(animal_bp, url_prefix='/api/animales')

@app.route('/')
def index():
    return "Bienvenido a la API de Animales. Visita /api/animales para más información."

if __name__ == '__main__':
    app.run(debug=True)
