from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/student/<regno>')
def get_student_status(regno):
    r = requests.get('http://db:5432/student/' + regno)
    if r.status_code == 200:
        return jsonify(r.json())
    else:
        return 'Error: Could not retrieve student data.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
