#!/usr/bin/python3
'''is this thing so tedious hmmm perfect choice for me though
'''


from os import getenv
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views

app = Flask(__name__)


CORS(app, resources={r'/api/v1/*': {'origins': '0.0.0.0'}})

app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_engine(exception):
    '''
    why is this thing so tedious hmmm perfect choice for me though
    '''
    storage.close()


@app.errorhandler(404)
def not_found(error):
    '''
    why is this thing so tedious hmmm perfect choice for me though
    '''
    response = {'error': 'Not found'}
    return jsonify(response), 404


if __name__ == '__main__':
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=HOST, port=PORT, threaded=True)
