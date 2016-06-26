from flask import Flask, Response
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from services import TwitterService
import json
import os
import tweepy

app = Flask(__name__)
app.config['REDIS_URL'] = os.environ['REDIS_URL']

redis_store = FlaskRedis(app)
api = Api(app)

twitterService = TwitterService(consumer_key=os.environ['consumer_key'],
    consumer_secret=os.environ['consumer_secret'],
    access_token=os.environ['access_token'],
    access_token_secret=os.environ['access_token_secret'])

class Trend(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('lat', type=float)
        parser.add_argument('lon', type=float)
        args = parser.parse_args()

        data = twitterService.getTrends(lat=args['lat'], lon=args['lon'])
        return Response(json.dumps(data), status=200, mimetype='application/json')

class User(Resource):
    def get(self):
        return Response(json.dumps(data), status=200, mimetype='application/json')

    def post(self):
        return ""

api.add_resource(User, '/users')
api.add_resource(Trend, '/trends')

if __name__ == '__main__':
	app.run(debug=True)
