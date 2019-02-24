from account import Account, load_all

from flask import Flask, send_from_directory, render_template
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
        a = Account(handle)
        if a.ok:
            accounts[handle] = a
            return accounts[handle].to_json(), 201
        else:
            return "Account not found", 404

    def put(self, handle):
        if handle in accounts:
            a = Account(handle)
            if a.ok:
                accounts[handle] = a
                return accounts[handle].to_json(), 200
            else:
                return "Account not found", 404
        a = Account(handle)
        if a.ok:
            accounts[handle] = a
            return accounts[handle].to_json(), 201
        else:
            return "Account not found", 404

@app.route('/')
def index():
    return send_from_directory("./dist", "index.html")
    
@app.route('/<path:filename>')
def serve(filename):
    return send_from_directory("./dist", filename)

api.add_resource(Profile, "/profile/<string:handle>")
app.run(debug=True)
