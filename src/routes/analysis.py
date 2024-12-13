from flask import request ,Blueprint;
from src.services.analysis import accident_frequency
from src.services.analysis import critical_days_hours
from src.services.analysis import Types_of_Accidents
from src.services.analysis import analyze_weather_conditions
from src.services.analysis import accident_distribution_by_city

analisis_bp = Blueprint("analisis",__name__)

@analisis_bp.route("/accident-frequency", methods=["GET"])
def accident_frequency_route():
    group_by = request.args.get('group_by', 'YEAR')
    resultado = accident_frequency(group_by)
    return resultado

@analisis_bp.route("/accident-distribution-by-city", methods=["GET"])
def accident_distribution_by_city2():
    resultado = accident_distribution_by_city()
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
