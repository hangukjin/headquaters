from flask import Flask
from flask import request
from flask_restful import Resource, Api
from flask_restful import reqparse
import json
import random
import redis

app = Flask(__name__)
api = Api(app)

class Sales(Resource):

    def post(self):

        print(request.json)

        if random.random() > 0.5:
            return True
        else:
            return False

api.add_resource(Sales, '/headquaters')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8086, debug=True)