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
    
@jwt_required()
def get_item(name):
    item = ItemModel.query.filter_by(name=name).first()
    if item:
        return jsonify({"id": item.id, "name": item.name, "price": item.price, "store_id": item.store_id})
    return {"message": "Item not found"}, 404

def update_item(name):
    data = request.get_json()

    # Verifica que el store_id exista
    store = StoreModel.query.get(data['store_id'])
    if not store:
        return {"message": "Store not found"}, 404

    item = ItemModel.query.filter_by(name=name).first()
    if item:
        item.price = data['price']
        item.store_id = data['store_id']
    else:
        item = ItemModel(name=name, **data)
        db.session.add(item)

    db.session.commit()
    return jsonify({"id": item.id, "name": item.name, "price": item.price, "store_id": item.store_id})

def delete_item(name):
    item = ItemModel.query.filter_by(name=name).first()
    if item:
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted."}
    return {"message": "Item not found"}, 404

def get_all_items():
    items = ItemModel.query.all()
    return jsonify({"items": [
        {"id": item.id, "name": item.name, "price": item.price, "store_id": item.store_id} for item in items
    ]})
    

