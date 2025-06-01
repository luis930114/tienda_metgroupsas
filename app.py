from flask import Flask
from config import Config
from extensions import db, jwt

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt.init_app(app)

with app.app_context():
    db.create_all()

# Registrar blueprints
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)
