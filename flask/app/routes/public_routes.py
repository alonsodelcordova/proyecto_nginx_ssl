from flask import Blueprint, request, jsonify, render_template, session, redirect
from app.models.user_model import User, Token

router_app = Blueprint('public', __name__)

@router_app.route('/')
def login_get():
    return render_template('login.html')


@router_app.route('/register')
def register_get():
    return render_template('register.html')


@router_app.route('/logout', methods=['GET'])
def logout():
    token = session.pop('user_token', None)
    if token:
        Token.query.filter_by(token=token).first().delete()
    session.clear()
    return redirect('/')


@router_app.route('/login', methods=['POST'])
def login():
    username = request.get_json().get('email')
    password = request.get_json().get('password')
    
    user_exists = User.query.filter_by(email=username).first()
    
    if user_exists and user_exists.verify_password(password):
        token = user_exists.generate_token()
        session['user_id'] = user_exists.id
        session['user_name'] = user_exists.name
        session['user_email'] = user_exists.email
        session['user_token'] = token
        return jsonify({
            'token': token,
            'user': user_exists.to_dict()
        })
    else:
        return jsonify({'message': 'Credenciales inválidas'}), 401

@router_app.post('/register')
def register():
    name = request.json.get('name')
    email = request.json.get('email')
    password = request.json.get('password')
    user = User(name, email, password)
    user.save()
    return jsonify({
        'message': 'Usuario creado correctamente'
    })
    
