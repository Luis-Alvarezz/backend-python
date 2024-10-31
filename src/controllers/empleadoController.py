from flask import jsonify, request
from services.empleado_service import empleadoService

class EmpleadoController:
  @staticmethod # Para que NO cambie ningun parámetro
  def get_all():
    empleados = empleadoService.get_all()
    return jsonify(empleados) # Retornamos el Objeto en formato JSON
  
  @staticmethod
  def get_by_id(empleado_id):
    empleado_id = empleadoService.get_by_id(empleado_id_id)
    return jsonify(empleado_id)
  
  @staticmethod
  def create_empleado():
    data = request.get_json()
    response = empleadoService.create_empleado(data)
    return jsonify(response)
  
  # Borrar, Actualizar, y lo que falte del CRUD ====================