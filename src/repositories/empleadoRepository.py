import firebase_admin
from firebase_admin import credentials, firestore
from models.empleadoModel import Empleado

cred = credentials.Certificate("RURA_AARCHIVO")
firebase_admin.initialize_app(cred)
db = firestore.client()
collection = 'empleados_python'

class EmpleadoRepository:
  @staticmethod
  def get_all():
    empleados = db.collection(collection)
    return [doc.to_dict() for doc in empleados.stream() ] # stream => async/await primitivos de alto nivel para trabajar con conexiones de red.
  # los streams permiten enviar y recibir datos sin utilizar callbacks y tranportes de bajo nivel.
  
  @staticmethod
  def create_empleado(data):
    db.collection(collection).add(data)
    
  @staticmethod
  def get_by_user(username):
    docs = db.collection.where(collection).where("usuario", "==", username).stream()
    
    for doc in docs:
      return Empleado.from_dict(doc.to_dict())
    return None