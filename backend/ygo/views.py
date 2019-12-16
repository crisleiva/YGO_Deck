from ygo import app, api_communicator

@app.route('/', methods=['GET'])
def index():
	return "hello world"

@app.route('/api/v1/cards/all', methods=['GET'])
def all_cards():
	return api_communicator.api_call()

@app.route('/api/v1/card/name/<name>', methods=['GET'])
def find_card_by_name(name):
	return api_communicator.find_by_name(name)


@app.route('/api/v1/card/level/<level>', methods=['GET'])
def find_card_by_level(level):
	return api_communicator.find_by_level(level)

@app.route('/api/v1/card/arch/<arch>', methods=['GET'])
def find_by_arch(arch):
	return api_communicator.find_cards_by_archetype(arch)