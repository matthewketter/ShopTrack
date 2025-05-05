from flask import Blueprint, jsonify, request
from models import Product

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# Using same products list for simplicity
from routes.products import products

@admin_bp.route('/add-product', methods=['POST'])
def add_product():
    new_product_data = request.json
    new_product = Product(
        id=len(products) + 1,
        name=new_product_data.get('name'),
        price=new_product_data.get('price')
    )
    products.append(new_product)
    return jsonify({"message": "Product added", "product": vars(new_product)}), 201
