from flask import Blueprint;
from src.services.accident_service import list_accident

accidentes_bp = Blueprint("accidentes",__name__)


@accidentes_bp.route("/",methods=["GET"])
def list_accidents_route():
    accidents = list_accident()
    return accidents


