from flask import Blueprint, jsonify, request, abort
from storage import cart, products

cart_bp = Blueprint('cart', __name__, url_prefix='/cart')

@cart_bp.route('/', methods=['GET'])
def view_cart():
    return jsonify(cart), 200

@cart_bp.route('/', methods=['POST'])
def add_to_cart():
    product_id = request.json.get('product_id')
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        abort(404, description="Product not found")
    cart.append(product)
    return jsonify({"message": "Product added to cart", "cart": cart}), 201

@cart_bp.route('/', methods=['DELETE'])
def clear_cart():
    cart.clear()
    return jsonify({"message": "Cart cleared"}), 200
