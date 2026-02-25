from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json or {}
    msg = data.get('message', '')
    # placeholder response — replace with model inference
    return jsonify({"response": f"Echo: {msg}"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
