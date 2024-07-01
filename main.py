import flask
from flask import request

app = flask.Flask(__name__)

@app.route('/')
def home(): 
    return 'Hello, Flask!'


@app.route('/index')
def index():
    index = request.args.get('index')
    return index




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
