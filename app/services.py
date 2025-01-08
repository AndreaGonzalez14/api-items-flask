from flask import Flask, request
from flask_restful import Resource
from items_base import items


class HelloWorld(Resource):

    def get(self):
        return "Hello World", 200


def get_item_by_id(item_id):
    for item in items:
        if item['id'] == item_id:
            return item
    return None


class ItemsCollection(Resource):

    def get(self):
        return items, 200

    def post(self):
        try:
            data = request.get_json()

            if 'name' not in data or 'price' not in data or data['price'] < 0:
                return {'message': 'Invalid data'}, 400

            new_item = {
                'id': len(items) + 1,
                'name': data['name'],
                'price': data['price'],
                'stock': data['stock'],
                'available': data.get('available', True)
            }
            items.append(new_item)
            return items, 201
        except Exception as e:
            return {'message': 'Error creating new item'}, 500


class Items(Resource):

    def get(self, item_id):
        result = [item for item in items if item['id'] == item_id]
        if not result:
            return {'message': 'Item not found'}, 404
        return result, 200

    def put(self, item_id):
        try:
            data = request.get_json()

            item = get_item_by_id(item_id)

            if not item:
                return {'message': 'Item not found'}, 404

            item['name'] = data.get('name', item['name'])
            item['price'] = data.get('price', item['price'])
            item['stock'] = data.get('stock', item['stock'])
            item['available'] = data.get('available', item['available'])

            return item, 200

        except Exception:
            return "Error to update item", 500

    def delete(self, item_id):
        try:
            data = request.get_json()

            item = get_item_by_id(item_id)

            if not item:
                return {'message': 'Item not found'}, 404

            items.remove(item)

            return items, 200

        except Exception:
            return "Error to delete item", 500
