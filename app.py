from flask import Flask, Response
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
import json
import os

app = Flask(__name__)
app.config['REDIS_URL'] = os.environ['REDIS_URL']

redis_store = FlaskRedis(app)
api = Api(app)

class User(Resource):
    def get(self):
        return Response(json.dumps(data), status=200, mimetype='application/json')

    def post(self):
        return ""

api.add_resource(User, '/')

if __name__ == '__main__':
	app.run(debug=True)
