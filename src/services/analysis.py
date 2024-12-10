from flask import  Blueprint,jsonify
import matplotlib.pyplot as plt
from src.database.connection_DB import get_db_connection
import pandas as pd

def accident_frequency():

    conn = get_db_connection()
    cursor = conn.cursor()

    query ="SELECT YEAR, COUNT(*) AS numeroAños FROM DATE_ACCIDENT group BY YEAR ORDER BY numeroAños DESC"

    cursor.execute(query)
    resultados = cursor.fetchall()

    analisis=[]

    for fila in resultados:
        analisis.append({
            "year" : fila[0],
            "numeroAños" : fila[1]
        })


    conn.close()
    return jsonify(analisis)
    
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

   