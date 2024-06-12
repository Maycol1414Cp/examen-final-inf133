from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from app.models.user_model import User
from app.utils.decorators import jwt_required, roles_required


user_bp = Blueprint("usuario", __name__)


@user_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    name=data.get("name")
    email=data.get("email")
    password=data.get("password")
    phone=data.get("phone")
    rol=data.get("rol")

    if not name or not password:
        return jsonify({"error": "Se requieren nombre de usuario y contraseña"}), 400

    existing_user = User.find_by_username(name)
    if existing_user:
        return jsonify({"error": "El nombre de usuario ya está en uso"}), 400

    new_user = User(name, email,password, phone, rol)
    new_user.save()

    return jsonify({"message": "Usuario creado exitosamente"}), 201


@user_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = data.get("user")
    password = data.get("password")

    user = User.find_by_username(user)
    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(
            identity={"user": user, "rol": user.rol}
        )
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401


