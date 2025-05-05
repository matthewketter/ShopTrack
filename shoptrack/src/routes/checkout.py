from flask import Blueprint, jsonify, abort
from storage import cart

checkout_bp = Blueprint('checkout', __name__, url_prefix='/checkout')

@checkout_bp.route('/', methods=['POST'])
def place_order():
    if not cart:
        abort(400, description="Cart is empty")

    total = sum(item['price'] for item in cart)
    order_id = 1234  # In a real app this would be dynamically generated
    order = {
        "order_id": order_id,
        "items": cart.copy(),
        "total_amount": total
    }

    cart.clear()
    return jsonify({
        "message": "Order placed successfully",
        "order": order
    }), 201
