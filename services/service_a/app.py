from flask import Flask

app = Flask(__name__)

@app.route('/api/v1/hello', methods=['GET'])
def hello():
    return {"message": "Hello from Service A!"}, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001,debug=True)