from flask import Flask
from routes.products import products_bp
from routes.cart import cart_bp
from routes.checkout import checkout_bp
from routes.admin import admin_bp
from routes.webhooks import webhooks_bp

app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Welcome to ShopTrack API"}, 200

def create_app():
    app.register_blueprint(products_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(checkout_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(webhooks_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
