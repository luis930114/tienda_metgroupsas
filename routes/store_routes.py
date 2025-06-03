from flask import Blueprint
from controllers.store_controller import create_store

bp = Blueprint('store', __name__)

bp.route('/store/<string:name>', methods=['POST'])(create_store)
