from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# init app
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World'


# Run server
if __name__ == '__main__':
    app.run(debug=True)
