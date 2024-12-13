import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Cargar los archivos CSV
df_date = pd.read_csv(r"C:\Users\juan3\OneDrive\Documentos\UPTC\DB2\accident_project\src\data\date_accident.csv")
df_location = pd.read_csv(r"C:\Users\juan3\OneDrive\Documentos\UPTC\DB2\accident_project\src\data\location.csv")
df_accidents = pd.read_csv(r"C:\Users\juan3\OneDrive\Documentos\UPTC\DB2\accident_project\src\data\tabla_accidentes.csv")
df_conditions = pd.read_csv(r"C:\Users\juan3\OneDrive\Documentos\UPTC\DB2\accident_project\src\data\tabla_condiciones.csv")
df_victims = pd.read_csv(r"C:\Users\juan3\OneDrive\Documentos\UPTC\DB2\accident_project\src\data\collateral_damage.csv")
df_classes = pd.read_csv(r"C:\Users\juan3\OneDrive\Documentos\UPTC\DB2\accident_project\src\data\Class_of_accident.csv")

# Unir los datos por las claves relevantes
df_combined = pd.merge(df_accidents, df_date, on="id_date")
df_combined = pd.merge(df_combined, df_location, on="id_location")
df_combined = pd.merge(df_combined, df_conditions, on="id_condition")
df_combined = pd.merge(df_combined, df_victims, on="id_accident")
df_combined = pd.merge(df_combined, df_classes, on="id_class_accident")

# Codificar variables categóricas
label_encoders = {}
categorical_columns = ["weekday", "geometry", "territory", "surface_condition", "land", "weather_condition", "class_of_accident"]
for col in categorical_columns:
    le = LabelEncoder()
    df_combined[col] = le.fit_transform(df_combined[col])
    label_encoders[col] = le

# Definir la variable objetivo (y) como si hubo un accidente grave (por ejemplo, si 'n_muertos' > 0)
df_combined['accident_occurred'] = df_combined['n_muertos'].apply(lambda x: 1 if x > 0 else 0)

# Seleccionar características (X) y la nueva etiqueta binaria (y)
X = df_combined[["day", "month", "year", "time_of_accident", "weekday", "geometry", "territory", "surface_condition", "land", "weather_condition"]]
y = df_combined["accident_occurred"]  # Etiqueta binaria (1 = accidente ocurrió, 0 = no)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Usar un clasificador RandomForest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluar el modelo
y_pred = model.predict(X_test)
print("Reporte de clasificación:\n", classification_report(y_test, y_pred))
print("Matriz de confusión:\n", confusion_matrix(y_test, y_pred))

# Función para ingresar datos del caso hipotético y realizar la predicción
def get_prediction():
    print("\nPor favor ingrese los detalles del accidente hipotético:")
    
    month = int(input("Mes del accidente: "))
    year = int(input("Año del accidente: "))
    time_of_accident = int(input("Hora del accidente (en formato 24 horas): "))
    weekday = int(input("Día de la semana (0=domingo, 1=lunes, 2=martes, etc.): "))

    # Crear un DataFrame con los datos ingresados
    new_data = pd.DataFrame({
        "day": [1],
        "month": [month],
        "year": [year],
        "time_of_accident": [time_of_accident],
        "weekday": [weekday],
        "geometry": [1],
        "territory": [1],
        "surface_condition": [1],
        "land": [0],
        "weather_condition": [0]
    })

    # Realizar la predicción
    probabilidad = model.predict_proba(new_data)[:, 1]  # Obtener la probabilidad de que ocurra un accidente (1)

    # Mostrar el resultado como porcentaje
    print(f"Probabilidad de que ocurra un accidente: {probabilidad[0] * 100:.2f}%")

# Ejecutar la función para ingresar los datos y mostrar la predicción
get_prediction()