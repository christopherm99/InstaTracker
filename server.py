from account import Account, load_all

from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

accounts = load_all()

class Profile(Resource):
    def get(self, handle):
        if handle in accounts:
            return accounts[handle].to_json(), 200
        return "Account not found", 404
    
    def post(self, handle):
        if handle in accounts:
            return accounts[handle].to_json(), 200
        try:
            accounts[handle] = Account(handle)
            return accounts[handle].to_json(), 201
        except:
            return [], 404

    def put(self, handle):
        if handle in accounts:
            accounts[handle] = Account(handle)
            return accounts[handle].to_json(), 200
        try:
            accounts[handle] = Account(handle)
            return accounts[handle].to_json(), 201
        except:
            return [], 404

api.add_resource(Profile, "/profile/<string:handle>")
app.run(debug=True)
