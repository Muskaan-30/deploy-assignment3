from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    # Requirement: "Hello from lastname ECS Container"
    return "Hello from Fatima ECS Container."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)