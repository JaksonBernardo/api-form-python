from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from api.models.User import User
from api.extensions import db, jwt
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash

from datetime import timedelta

user_bp = Blueprint("user_bp", __name__, url_prefix = "/user")

@user_bp.route("/login", methods=["POST"])
def login():

    email_user = request.json.get("email-user")

    password = request.json.get("password")
    
    user = User.query.filter_by(email=email_user).first()

    if user:

        if not check_password_hash(user.password, password):

            return jsonify({"msg": "Senha incorreta"}), 401
        
        access_token = create_access_token(identity = str(user.id))
        
        refresh_token = create_refresh_token(identity=str(user.id))

        return jsonify(access_token = access_token, refresh_token=refresh_token), 200
    
    else:

        return jsonify({"msg": "Usuário não encontrado"}), 401

@user_bp.route("/token/refresh", methods=["POST"])
@jwt_required(refresh = True)
def refresh():

    current_user_id = get_jwt_identity()

    new_access_token = create_access_token(identity = current_user_id)

    return jsonify(access_token = new_access_token), 200



