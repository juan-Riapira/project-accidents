from flask import  Blueprint,jsonify
from src.database.connection_DB import  get_db_connection

accidentes_bp = Blueprint("accidentes", __name__)

    
def list_accident():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    #Colsultar bases de datos
    query = "SELECT * FROM Accident"
    cursor.execute(query)
    resultados = cursor.fetchall()
    if not resultados:
         return jsonify({"mensaje": "No se encontraron accidentes"}), 404
    
    accidentes=[]

    for fila  in resultados:
        accidentes.append({
            "id_accident": fila[0],
            "accident_time":fila[1],
            "id_location":fila[2],
            "id_condition":fila[3],
            "id_class_accident":fila[4],
            "id_date":fila[5]              

        })
        
    conn.close()
    return jsonify(accidentes)
    


