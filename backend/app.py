from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

ADMIN_USER = {
    "email": "hello@savvyfinance.com", 
    "password": "SavvyFinance@!"
}

@app.route('/')
def root():
    return jsonify({"message": "SavvyFinance API running!"})

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    if (data.get('email') == ADMIN_USER['email'] and 
        data.get('password') == ADMIN_USER['password']):
        return jsonify({
            "access_token": "token123",
            "user": {"email": ADMIN_USER['email'], "role": "admin"}
        })
    return jsonify({"error": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
