from flask_restful import Resource

class User(Resource):
    def get(self):
        return "Get to user"

    def post(self):
        return ""
