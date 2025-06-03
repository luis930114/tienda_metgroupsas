from flask import Blueprint
from controllers.store_controller import create_store, get_store, delete_store, get_all_stores

bp = Blueprint('store', __name__)

bp.route('/store/<string:name>', methods=['POST'])(create_store)
bp.route('/store/<string:name>', methods=['GET'])(get_store)
bp.route('/store/<string:name>', methods=['DELETE'])(delete_store)
bp.route('/stores', methods=['GET'])(get_all_stores)

