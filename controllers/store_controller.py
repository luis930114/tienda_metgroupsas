from flask import jsonify
from models.store import StoreModel
from extensions import db

def create_store(name):
    if StoreModel.query.filter_by(name=name).first():
        return {"message": "Store already exists."}, 400
    store = StoreModel(name=name)
    db.session.add(store)
    db.session.commit()
    return jsonify({"id": store.id, "name": store.name, "items": []})

def get_store(name):
    store = StoreModel.query.filter_by(name=name).first()
    if store:
        return jsonify({"id": store.id, "name": store.name, "items": [
            {"id": item.id, "name": item.name, "price": item.price, "store_id": item.store_id} for item in store.items
        ]})
    return {"message": "Store not found"}, 404

def delete_store(name):
    store = StoreModel.query.filter_by(name=name).first()
    if store:
        db.session.delete(store)
        db.session.commit()
        return {"message": "Store deleted."}
    return {"message": "Store not found"}, 404

def get_all_stores():
    stores = StoreModel.query.all()
    return jsonify({"stores": [
        {"id": store.id, "name": store.name, "items": [
            {"id": item.id, "name": item.name, "price": item.price, "store_id": item.store_id} for item in store.items
        ]} for store in stores
    ]})


