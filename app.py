from flask import Flask

app = Flask(__name__)


@app.route('/caca')
def hello_world():
    return 'La mata!'


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
