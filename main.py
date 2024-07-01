import flask

app = flask.Flask(__name__)

@app.route('/')
def home():
    return '我是flask!'

if __name__ == '__main__':
    app.run(Port=5000, debug=True)
