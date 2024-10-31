# Importar las cosas que vamos a utilizar:
from routes.empleados_routes import init_empleado_routes
from middleware.auth_middleware import require_auth
from flask import Flask

app = Flask(__name__) # Creamos instancia de la clase, siendo __name__ un atajo
# Siendo necesario para que Flask sepa enn donde buscar recursos como plantaillas y archivos estátivos.
app.config['SECRET_KEY'] = 'VAR_KEY_SECRET'

# Inicializmos las rutas 
init_empleado_routes(app)

#Definimos el middleware
app.before_request(require_auth)

if __name__ == '__main__':
  app.run(debug=True)