from flask import Flask, render_template, request
from datetime import datetime

app = Flask('lab05')
# flask run --host=0.0.0.0 --debug
@app.route('/',methods=['GET, POST'])
def some_page():
	t = datetime.now()
	s = t.strftime('%H:%M:%S')
	abc = request.args.get('param')
	print(s)
	return render_template('index.html', s=s, name=abc)
	
