from flask import Flask, render_template
from src.routes.accidents import accidentes_bp
from src.routes.analysis import analisis_bp

# Crear la única instancia de Flask
app = Flask(__name__, template_folder=r'C:\Users\juan3\OneDrive\Documentos\UPTC\DB2\accident_project\templates')

# Registrar los blueprints
app.register_blueprint(accidentes_bp, url_prefix="/api/accidentes")
app.register_blueprint(analisis_bp, url_prefix="/api/analisis")

# Ruta normal para cargar la plantilla
@app.route("/main")
def desplaga():
    print("Ruta de templates:", app.template_folder)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
