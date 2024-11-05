import jwt
from  flask import request, jsonify
from functools import wraps

SECRET_KEY = 'VAR_KEY_SECRET' 

def token_required(f):
  def decorated(*args, **kwargs):
    token = request.headers.get('Autorization')
    if not token:
      return jsonify({ 'message': 'Token is missing' }), 403
    
    try:
      jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError: 
      return jsonify({ 'message': 'Token Expired' }), 403
    except jwt.InvalidTokenError:
      return jsonify({ 'message': 'Token Inválido' }), 403
    return f(*args, **kwargs)
  return decorated