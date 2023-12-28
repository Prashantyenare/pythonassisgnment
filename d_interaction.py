from flask import Flask, request, current_app
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

# Create all database tables within the application context
with app.app_context():
    db.create_all()

class ItemListResource(Resource):
    def get(self):
        with app.app_context():
            items = Item.query.all()
            items_data = [{'id': item.id, 'name': item.name} for item in items]
            return {'items': items_data}

    def post(self):
        data = request.get_json()
        new_item = Item(name=data['name'])
        with app.app_context():
            db.session.add(new_item)
            db.session.commit()
            return {'item': {'id': new_item.id, 'name': new_item.name}}, 201

api.add_resource(ItemListResource, '/items')

if __name__ == '__main__':
    app.run(debug=True)
