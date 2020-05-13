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
        db = redis.Redis('localhost')

        json_dict = json.dumps(request.json, ensure_ascii=False).encode('utf-8')
        db.set(request.json["cafeId"], json_dict)

        #db.set("cafeId", request.json["salesSum"])

        if random.random() > 0.5:
            return True
        else:
            return False

api.add_resource(Sales, '/headquaters')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8086, debug=True)