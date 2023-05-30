from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from config.config import Config

from resources.roles import Roles

app = Flask(__name__)

app.config.from_object(Config)
api = Api(app)
CORS(app,supports_credentials=True,origins='*')


api.add_resource(Roles, '/roles')

if __name__ == '__main__':
    app.run(port=Config.PORT, host="0.0.0.0", debug=False)
