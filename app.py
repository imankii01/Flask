from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})


@app.route('/hii', methods=['GET'])
def hii():
    return jsonify({'message': 'Hii, World!'})

@app.route('/love', methods=['GET'])
def love():
    return jsonify({'message': 'love, World!'})

if __name__ == '__main__':
    app.run(debug=True)
    
