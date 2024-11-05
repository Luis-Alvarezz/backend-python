from flask import Flask
from routes.routes import routes

app = Flask(__name__) # Creamos instancia de la clase, siendo __name__ un atajo
# Siendo necesario para que Flask sepa enn donde buscar recursos como plantaillas y archivos estátivos.
# app.config['SECRET_KEY'] = 'VAR_KEY_SECRET' - Se puso en Middleware
app.register_blueprint(routes)


if __name__ == "__main__":
  app.run(debug=True)