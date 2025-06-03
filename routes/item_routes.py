from flask import Blueprint
from controllers.item_controller import create_item, get_item, update_item, delete_item, get_all_items

bp = Blueprint('item', __name__)

bp.route('/item/<string:name>', methods=['POST'])(create_item)
bp.route('/item/<string:name>', methods=['GET'])(get_item)
bp.route('/item/<string:name>', methods=['PUT'])(update_item)
bp.route('/item/<string:name>', methods=['DELETE'])(delete_item)
bp.route('/items', methods=['GET'])(get_all_items)

