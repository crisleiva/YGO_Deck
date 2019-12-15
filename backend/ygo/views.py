from ygo import app, helpers
from flask import jsonify

@app.route('/', methods=['GET'])
def index():
	return "hello world"

@app.route('/api/v1/cards/all', methods=['GET'])
def all_cards():
	return helpers.api_call()