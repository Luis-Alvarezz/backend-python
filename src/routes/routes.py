from flask import Blueprint
from controllers.empleadoController import EmpleadoController
from middleware.authMiddleware import token_required

empleadoController = EmpleadoController()
routes = Blueprint('routes', __name__)

# Ruta para obtener Todos los Empleados
# routes.add_url_rule('/empleados', 'get_all', token_required(empleadoController.get_all), methods=['GET'])
routes.add_url_rule('/empleados', 'get_all', empleadoController.get_all, methods=["GET"])

# Ruta para ID
routes.add_url_rule('/empleados/<id>', 'get_by_id', empleadoController.get_by_id, methods=["GET"])

# Ruta para Obtener empleado por usuario
routes.add_url_rule('/empleados/user/<username>', 'get_by_user', empleadoController.get_by_user, methods=["GET"])

# Ruta para Crear Empleado
routes.add_url_rule('/empleados', 'create_empleado', empleadoController.create_empleado, methods=["POST"])

# Ruta para actualizar empleado:
routes.add_url_rule('/empleados/<id>', 'update_empleado', empleadoController.update_empleado, methods=["PUT"])

# Ruta para eliminar Empleado:
routes.add_url_rule('/empleados/<id>', 'delete_empleado', empleadoController.delete_empleado, methods=["DELETE"])

# Omitir Token Required, solo dejamos la funcion, tambien dememos quitar la importación.  