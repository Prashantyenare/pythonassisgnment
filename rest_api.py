from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class ItemListResource(Resource):
    def get(self):
        return {'items': items}

    def post(self):
        data = request.get_json()
        new_item = {'name': data['name']}
        items.append(new_item)
        return {'item': new_item}, 201

api.add_resource(ItemListResource, '/items')

if __name__ == '__main__':
    app.run(debug=True)
