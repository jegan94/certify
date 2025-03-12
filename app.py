from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/login', methods=['POST'])
def greet():
    data = request.json  # Get JSON data from the request
    name = data.get("name", "Guest")
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == '__main__':
    app.run(debug=True)
