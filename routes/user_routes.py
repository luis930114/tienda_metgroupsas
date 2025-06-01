from flask import Blueprint
from controllers.user_controller import register, auth

bp = Blueprint('user', __name__)

bp.route('/register', methods=['POST'])(register)
bp.route('/auth', methods=['POST'])(auth)
