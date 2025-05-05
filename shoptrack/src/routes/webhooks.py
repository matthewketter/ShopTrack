from flask import Blueprint, jsonify

webhooks_bp = Blueprint('webhooks', __name__, url_prefix='/webhooks')

@webhooks_bp.route('/new-order', methods=['POST'])
def simulate_webhook():
    # This would POST data to an external webhook URL in real life
    return jsonify({"message": "Webhook triggered (stub)"}), 200
