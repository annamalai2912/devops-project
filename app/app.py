from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify(status="healthy")

@app.route('/')
def hello():
    host_name = socket.gethostname()
    return jsonify(
        message="Hello from DevOps Demo!",
        hostname=host_name
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)