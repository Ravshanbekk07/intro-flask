from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    print(request.path)
    print(request.method)
    print(request.headers)

    return 'Hello World!'

@app.route('/say-hello')
def say_hello():
    params = request.args
    name = params.get('name')
    return f'Hello <b>{name}</b>!'


if __name__ == '__main__':
    app.run(debug=True)
