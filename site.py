from flask import Flask, render_template, jsonify, request, make_response
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
	return render_template('index.html')

@app.route('/new_restaurant', method=['POST'])
def new_restaurant():


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8001, debug=True)
