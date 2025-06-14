from functools import wraps
from flask import request, session, redirect
from app.models.user_model import Token, User

# para validar token - API REST
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token requerido'}), 403
        
        token_obj = Token.query.filter_by(token=token).first()
        if not token_obj:
            return jsonify({'message': 'Token inválido'}), 401
        
        # Opcional: obtener usuario asociado
        user = User.query.get(token_obj.user_id)
        if not user:
            return jsonify({'error': 'Usuario no encontrado'}), 401

        return f(user, *args, **kwargs) 
    
    return decorated

# para validar token - SESSION - Flask pages
def session_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return redirect('/')
        current_user = User.query.get(session['user_id'])
        token = Token.query.filter_by(user_id=current_user.id).first()
        if token.token != session['user_token']:
            return redirect('/')
        
        return f(*args, **kwargs, current_user=current_user)
    return decorated
