from flask import jsonify, request
from services.empleadoService import EmpleadoService

class EmpleadoController:
  def __init__(self):
    self.service = EmpleadoService()
    
  # @staticmethod # Para que NO cambie ningun parámetro
  def get_all(self):
    empleados = self.service.get_all()
    return jsonify([empleado.to_dict() for empleado in empleados]) # Retornamos el Arreglo en formato JSON
  
  # @staticmethod
  def get_by_id(self, id):
    user_id = self.service.get_by_id(id)
    return jsonify(user_id.to_dict()) if user_id else ('Empleado no encontrado', 404)
  
  
  def get_by_user(self, username):
    empleado = self.service.get_by_user(username)
    return jsonify(empleado.to_dict()) if empleado else ('Empleado no encontrado en Controlador', 404)
  
  # @staticmethod
  def create_empleado(self):
    data = request.get_json()
    try:
      user_id = self.service.create_empleado(data)
      return jsonify({ 'id': user_id }), 201
    except ValueError as e: return jsonify({ 'error': str(e) }), 400
  
  def update_empleado(self, id):
    data = request.get_json()
    self.service.update_empleado(id, data)
    return jsonify({ 'message': 'Empleado Actualizado' }), 200
  
  def delete_empleado(self, id):
    self.service.delete_user(id)
    return jsonify({ 'message': 'Empleado Borrado' }), 200