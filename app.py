from flask import Flask, request,render_template
from main import read_file
import requests

app = Flask(__name__)


@app.route('/read_file')
def read_data():
	try:
	    file_name = request.args.get('file_name','file1.txt')
	    start = request.args.get('start',None)
	    end = request.args.get('end',None)
	    data = read_file(file_name,start, end)
	    return render_template("index.html",text = data)
	except requests.exceptions.RequestException as e:
		pass


if __name__ == '__main__':
    app.run(debug=True)