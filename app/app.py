from flask import Flask
from flask_restful import Api
from services import *


app = Flask(__name__)
api = Api(app)


api.add_resource(HelloWorld, '/api/hello')
api.add_resource(ItemsCollection, '/api/items')
api.add_resource(Items, '/api/items/<int:item_id>')


@app.route('/')
def index() -> str:
    return "API ITEMS - TEST INOVA SOLUTIONS"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)
