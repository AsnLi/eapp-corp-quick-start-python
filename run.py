# -*- coding:utf-8 -*-

from flask import Flask, request, jsonify
from login import Login
app = Flask(__name__)

# Registration login event
@app.route('/login', methods=['POST'])
def user_login():
    query = request.json # Set the value to request.form if error is reported

    return jsonify(Login(query['authCode']).get_data())

# Start the service
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)