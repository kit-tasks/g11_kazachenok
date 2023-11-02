
from flask import Flask, request

app = Flask('lab01')
# flask run --host=0.0.0.0 --debug
@app.route('/test', methods=['GET', 'POST']) 
def my_form():
	abc=''
	if request.method == 'GET':
		abc = request.args.get('param1')
		a = request.args.get('param3')
		b = request.args.get('param4')
	if request.method == 'POST':
		abc = request.form.get('param2')
	return 'hello, ' + a + '!'
