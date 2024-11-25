from flask import Blueprint, jsonify, render_template
from models.perro import Perro
from models.gato import Gato
from models.huron import Hurón
from models.boa_constrictor import BoaConstrictor

animal_bp = Blueprint('animal_bp', __name__)

# Instancias de los animales
animales = [
    Perro("Firulais", 5, "Golden Retriever"),
    Gato("Miau", 2, "Siamés"),
    Hurón("Zippy", 3),
    BoaConstrictor("Slinky", 8, "2.5 metros")
]

@animal_bp.route('/', methods=['GET'])
def listar_animales():
    """Devuelve la lista de animales en JSON."""
    return jsonify([animal.to_dict() for animal in animales])

@animal_bp.route('/<especie>', methods=['GET'])
def obtener_animal(especie):
    """Devuelve la información de un animal específico."""
    animal = next((a for a in animales if a.especie.lower() == especie.lower()), None)
    if animal:
        return jsonify(animal.to_dict())
    return jsonify({"error": "Animal no encontrado"}), 404

@animal_bp.route('/vista', methods=['GET'])
def vista_animales():
    """Muestra la página web con información de los animales."""
    return render_template('animal.html', animales=animales)
