
from flask import Flask, request
# flask run --host=0.0.0.0 --debug

app = Flask('lab04')
@app.route('/checkboxes',methods=['GET', 'POST'])
def my_checkbox():
	if request.method == 'GET':
		o1= request.args.get('op1')
		o2= request.args.get('op2')
		if o1 == None:
			if o2 == None:
				return 'booth option is not select'
			return 'option 1 not select'
		if o2 == None:
			return 'option 2 not select'
		return 'booth option is selected'
	if request.method == 'POST':
		o1 = request.form.get('op1')
		o2 = request.form.get('op2')
		if o1 == None:
			if o2 == None:
				return 'booth option is not select'
			return 'option 1 not select'
		if o2 == None:
			return 'option 2 not select'
		return 'booth option is selected'
