from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    # Add authentication logic here
    return jsonify({'message': 'Login successful', 'username': username})

if __name__ == '__main__':
    app.run(debug=True)