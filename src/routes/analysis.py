from flask import Blueprint;
from src.services.analysis import accident_frequency

analisis_bp = Blueprint("analisis",__name__)

@analisis_bp.route("/", methods=["GET"])
def accident_frequency_route():
    resultado = accident_frequency()
    return resultado