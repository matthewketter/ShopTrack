from flask import Blueprint, jsonify
from storage import products  # <-- correct shared import

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/', methods=['GET'])
def list_products():
    return jsonify(products), 200
