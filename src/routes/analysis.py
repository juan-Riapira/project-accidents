from flask import Blueprint;
from src.services.analysis import accident_frequency
from src.services.analysis import critical_days_hours
from src.services.analysis import Types_of_Accidents
from src.services.analysis import analyze_weather_conditions

analisis_bp = Blueprint("analisis",__name__)

@analisis_bp.route("/", methods=["GET"])
def accident_frequency_route():
    resultado = accident_frequency()
    return resultado

@analisis_bp.route("/critical-days-hours", methods=["GET"])
def critical_days_hours_report():
    resultado = critical_days_hours()
    return resultado

@analisis_bp.route("/Types-of-Accident", methods=["GET"])
def Types_of_Accidents_report():
    resultado = Types_of_Accidents()
    return resultado

@analisis_bp.route("/analyze-weather-conditions", methods=["GET"])
def analyze_weather_conditions_report():
    resultado = analyze_weather_conditions()
    return resultado
