from flask import jsonify
from src.database.connection_DB import get_db_connection
import pandas as pd


def accident_frequency(group_by="YEAR"):
 
    conn = get_db_connection()
    cursor = conn.cursor()

    if group_by not in ["YEAR", "MONTH"]:
        conn.close()
        return jsonify({"error": "El parámetro 'group_by' debe ser 'YEAR' o 'MONTH'"}), 400
    query=""
    if group_by == "YEAR":
        query = """
            SELECT YEAR, COUNT(*) AS numeroAccidentes
            FROM DATE_ACCIDENT
            GROUP BY YEAR
            ORDER BY numeroAccidentes DESC
        """
    elif group_by == "MONTH":
        query = """
            SELECT YEAR || '-' || TO_CHAR(MONTH, 'FM00') AS periodo, 
            COUNT(*) AS numeroAccidentes
            FROM DATE_ACCIDENT
            GROUP BY YEAR, MONTH
            ORDER BY YEAR ASC, MONTH ASC
        """

    cursor.execute(query)
    resultados = cursor.fetchall()

    analisis = []
    for fila in resultados:
        analisis.append({
            "periodo": fila[0],
            "numeroAccidentes": fila[1]
        })

    conn.close()

    return jsonify(analisis)
    
def accident_distribution_by_city():

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
                SELECT 
                L.geometry, 
                COUNT(A.id_accident) AS total_accidentes
            FROM 
                accident A
            JOIN 
                location L ON A.id_location = L.id_location
            GROUP BY 
                L.geometry
            ORDER BY 
                total_accidentes DESC
    """

    cursor.execute(query)
    resultados = cursor.fetchall()

    distribucion = []
    for fila in resultados:
        distribucion.append({
            "ciudad": fila[0],
            "total_accidentes": fila[1]
        })

    conn.close()

    return jsonify(distribucion)

def critical_days_hours():
   conn = get_db_connection()
   cursor = conn.cursor()

   query = """SELECT 
                DA.weekday AS dia_semana, 
                A.accident_time AS hora_comun, 
                COUNT(*) AS total_accidentes
            FROM 
                Accident A
            JOIN 
                Date_Accident DA ON A.id_date = DA.id_date
            GROUP BY 
                DA.weekday, A.accident_time
            ORDER BY 
                COUNT(*) DESC, DA.weekday
            FETCH FIRST 7 ROWS ONLY
            """

   cursor.execute(query)
   resultados = cursor.fetchall()
   analisis = []
   for fila in resultados:
        analisis.append({
            "dia_semana": fila[0],
            "hora": fila[1],
            "total_accidentes": fila[2]
        })

   conn.close()
   return jsonify(analisis)

def Types_of_Accidents():

    conn = get_db_connection()
    cursor = conn.cursor()

    query ="""SELECT 
                CA.class_of_accident AS tipo_accidente, 
                COUNT(*) AS total_accidentes            
            FROM 
                Accident A
            JOIN 
                Class_of_accident CA ON A.id_class_accident = CA.id_class_of_accident
            GROUP BY 
                CA.class_of_accident
            ORDER BY 
                total_accidentes DESC   
         """

    cursor.execute(query)
    resultados = cursor.fetchall()

    analisis=[]

    for fila in resultados:
        analisis.append({
            "Tipo_Accidente" : fila[0],
            "total_accidentes" : fila[1]
        })


    conn.close()
    return jsonify(analisis)

def analyze_weather_conditions():
    # Conectar a la base de datos
    conn = get_db_connection()
    cursor = conn.cursor()

    # Ejecutar la consulta SQL
    query = """
    SELECT 
        C.weather_condition AS condicion_climatica,
        COUNT(*) AS total_accidentes
    FROM 
        Accident A
    JOIN 
        Conditions C ON A.id_condition = C.id_conditions
    GROUP BY 
        C.weather_condition
    ORDER BY 
        total_accidentes DESC
    """

    cursor.execute(query)
    resultados = cursor.fetchall()

    analisis=[]

    for fila in resultados:
        analisis.append({
            "condicion_climatica" : fila[0],
            "total_accidentes" : fila[1]
        })


    conn.close()
    return jsonify(analisis)

   