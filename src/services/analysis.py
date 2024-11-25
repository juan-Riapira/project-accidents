from flask import  Blueprint,jsonify
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
    