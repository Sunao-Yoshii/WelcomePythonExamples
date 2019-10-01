from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    respondData = {
        'message': 'Hello',
        'status': 100,
        'array_value': [1, 2, 4, 8, 16]
    }
    return jsonify(respondData)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
