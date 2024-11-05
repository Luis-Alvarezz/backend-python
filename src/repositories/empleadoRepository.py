from config.firebaseConfig import initialize_firebase
from models.empleadoModel import Empleado

# cred = credentials.Certificate("RURA_AARCHIVO") -> Ya no se necesita porque tenemos archivo de Conf propio
# firebase_admin.initialize_app(cred)
# db = firestore.client()
# collection = 'empleados_python'

class EmpleadoRepository:
  def __init__(self):
    self.db = initialize_firebase()
    self.collection = self.db.collection('empleados_python')
    
  def get_all(self):
    empleados = [Empleado.from_dict(doc.to_dict()) for doc in self.collection.stream()] # stream => async/await primitivos de alto nivel para trabajar con conexiones de red.
    return empleados 
  # los streams permiten enviar y recibir datos sin utilizar callbacks y tranportes de bajo nivel.
  
  def create_empleado(self, empleado_nuevo):
    doc = self.collection.document()
    doc.set(empleado_nuevo.to_dict())
    
    return doc.id
    
  def get_by_user(self, username):
    docs = self.collection.where("usuario", "==", username).stream()
    
    for doc in docs:
      return Empleado.from_dict(doc.to_dict())
    return None
  
  def get_by_id(self, id):
    doc = self.collection.document(id).get() # document se refiere 
    return Empleado.from_dict(doc.to_dict()) if doc.exists else None
  
  def update_empleado(self, id, data):
    self.collection.document(id).update(data)
    
  def delete_user(self, id):
    self.collection.document(id).delete()