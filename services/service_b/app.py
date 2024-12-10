from flask import Flask

app = Flask(__name__)

@app.route('/api/v1/status', methods=['GET'])
def status():
    return {"status": "Service B is up!"}, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002,debug=True)