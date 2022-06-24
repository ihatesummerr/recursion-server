from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine


app = Flask(__name__)
CORS(app)

app.config['MONGODB_SETTINGS'] = {
    'db': 'recursion',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine(app)


@app.route('/', methods=['GET'])
def index():
    return 'Server is up and running'


import recursion.schema
import recursion.routes.user
import recursion.routes.event
import recursion.routes.student


