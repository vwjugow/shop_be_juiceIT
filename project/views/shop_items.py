import json

from flask import request

from project.models import ShopItem, db
from . import shop_items_blueprint


@shop_items_blueprint.after_request
def after_request(response):
    header = response.headers
    header["Access-Control-Allow-Origin"] = "*"
    header["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, PATCH, DELETE"
    header["Access-Control-Allow-Headers"] = "Content-Type"
    header["Content-Type"] = "application/json"
    return response


@shop_items_blueprint.route("/shopitem", methods=["GET"])
def fetch():
    shop_items = ShopItem.query.all()
    all_items = []
    for item in shop_items:
        new_item = {
            "id": item.id,
            "name": item.name,
            "description": item.description,
            "price": item.price,
            "image_title": item.image_title,
            "image_url": item.image_url,
        }
        all_items.append(new_item)
    return json.dumps(all_items), 200


@shop_items_blueprint.route("/shopitem", methods=["POST"])
def add():
    data = request.get_json()
    name = data.get("name")
    price = data.get("price")
    description = data.get("description")
    image_title = data.get("image_title")
    image_url = data.get("image_url")
    instance = ShopItem(name, price, description, image_title, image_url)
    db.session.add(instance)
    db.session.commit()
    return json.dumps({"result": "Added"}), 201


@shop_items_blueprint.route("/shopitem/<item_id>", methods=["DELETE"])
def remove(item_id):
    item = ShopItem.query.filter_by(id=item_id)
    if item:
        item.delete()
        return json.dumps({"message": "Deleted"}), 200
    else:
        return json.dumps({"message": "Item with given id was not found"}), 404


@shop_items_blueprint.route("/shopitem/<item_id>", methods=["PATCH"])
def edit(item_id):
    data = request.get_json()
    new_price = data["price"]
    item = ShopItem.query.filter_by(id=item_id).all()
    if item:
        item = item[0]
        item.price = new_price
    return json.dumps({"message": "Edited"}), 200
