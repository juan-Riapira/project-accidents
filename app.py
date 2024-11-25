from flask import Flask
from src.routes.accidents import accidentes_bp
from src.routes.analysis import analisis_bp


app = Flask(__name__)


# Registrar los blueprints (rutas organizadas)
app.register_blueprint(accidentes_bp, url_prefix="/api/accidentes")
app.register_blueprint(analisis_bp,url_prefix="/api/analisis")
if __name__ == "__main__":
    app.run(debug=True)

