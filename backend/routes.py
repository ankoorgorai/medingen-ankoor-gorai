from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required
from models import Product, Review
from database import db

api = Blueprint('api', __name__)

@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data['username'] == 'admin' and data['password'] == 'admin':
        token = create_access_token(identity='admin')
        return jsonify(access_token=token)
    return jsonify(message='Invalid credentials'), 401

@api.route('/products', methods=['GET'])
@jwt_required()
def get_products():
    products = Product.query.all()
    return jsonify([
        {"id": p.id, "name": p.name, "description": p.description,
         "salt_content": p.salt_content, "price": p.price}
        for p in products
    ])
