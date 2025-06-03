from flask import request, jsonify
from flask_jwt_extended import jwt_required
from models.item import ItemModel
from models.store import StoreModel
from extensions import db

def create_item(name):
    data = request.get_json()
    if not StoreModel.query.get(data['store_id']):
        return {"message": "Store not found"}, 404
    item = ItemModel(name=name, price=data['price'], store_id=data['store_id'])
    db.session.add(item)
    db.session.commit()
    return jsonify({"id": item.id, "name": item.name, "price": item.price, "store_id": item.store_id})
    

