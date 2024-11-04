# Requeriremos lo del Repositorio:
from repositories.empleado_repository import empleadoRepository
from utils.encryption_util import encrypt_password
from utils.token_util import generate_token
from utils.token_util import generate_token
import time

class EmpleadoService:
  @staticmethod
  def get_all():
    return empleadoRepository.get_all()
  
  @staticmethod
  def create_empleado(data):
    if empleadoRepository.get_by_user(data['usuario']):
      return { "error": "Usuario YA existe" }
    
    data['password'] = encrypt_password(data['password'])
    empleadoRepository.create_empleado(data)
    token = generate_token(data['usuario'])
    return { 
            "message": "Empleado Registrado",
            "token": token
           }
  
  @staticmethod
  def get_by_id():
    return empleadoRepository.get_ 