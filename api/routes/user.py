from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import jwt_required, get_jwt_identity
from api.models.User import User
from api.extensions import db, jwt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash

from datetime import timedelta

user_bp = Blueprint("user_bp", __name__, url_prefix = "/user")

@user_bp.route("/login", methods=["POST"])
def login():

    username = request.json.get("username")
    password = request.json.get("password")
    
    user = User.query.filter_by(username=username).first()

    if user:

        if not check_password_hash(user.password, password):

            return jsonify({"msg": "Senha incorreta"}), 401
        
        access_token = create_access_token(identity = str(user.id), expires_delta = timedelta(hours = 1))

        return jsonify(access_token = access_token), 200
    
    else:

        return jsonify({"msg": "Usuário não encontrado"}), 401


@user_bp.route("/my-forms", methods=["GET"])
@jwt_required()
def my_forms():

    current_user_id = get_jwt_identity()

    user = User.query.get(current_user_id)

    company = user.company
    forms = company.forms
    forms_list = []
    for form in forms:
        forms_list.append({
            "id": form.id,
            "title": form.title,
            "type": form.type
        })
    
    return jsonify({"forms": forms_list}), 200
