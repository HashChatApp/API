from flask import Flask
from flask_restful import Api
from routes import User
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://bhqmvvps:bza2ikra0W6P19m1gW-DWHfLw07Ku_Ld@pellefant.db.elephantsql.com:5432/bhqmvvps'

db = SQLAlchemy(app)
api = Api(app)


api.add_resource(User, '/')

if __name__ == '__main__':
	app.run(debug=True)
