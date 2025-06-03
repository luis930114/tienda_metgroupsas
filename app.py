from flask import Flask
from config import Config
from extensions import db, jwt
from routes.user_routes import bp as user_bp
from routes.store_routes import bp as store_bp
from routes.item_routes import bp as item_bp
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt.init_app(app)

with app.app_context():
    db.create_all()

# Registrar blueprints
app.register_blueprint(user_bp)
app.register_blueprint(store_bp)
app.register_blueprint(item_bp)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
