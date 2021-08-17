from flask import Flask, jsonify
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)

@app.route('/hello')
def hello_world():
	return "<p> Hello World !"

@app.route('/calculate/<string:operator>/<int:first_operand>/<int:second_operand>')
def calculate(operator, first_operand, second_operand):
	result = ''
	if operator == 'add':
		result = str(first_operand + second_operand)
	elif operator == 'subtract':
		result = str(first_operand - second_operand)
	elif operator == 'multiply':
		result = str(first_operand * second_operand)
	elif operator == 'divide':
		result = str(first_operand / second_operand)

	return jsonify({'result':result})

if __name__ == '__main__':
	app.run(debug=True)



