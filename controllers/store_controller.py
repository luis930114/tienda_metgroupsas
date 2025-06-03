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

