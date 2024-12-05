from functools import wraps
from flask import request, jsonify, current_app
import jwt

def jwt_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            try:
                token = auth_header.split(' ')[1]
            except IndexError:
                pass

        if not token:
            return jsonify({'error': 'Token is missing'}), 401

        try:
            jwt.decode(token, current_app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
        except:
            return jsonify({'error': 'Token is invalid'}), 401

        return f(*args, **kwargs)
    return decorated