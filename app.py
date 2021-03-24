from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# init app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://new_user:news@localhost:5432/news'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(50))
    title = db.Column(db.String(150))


@app.route('/')
def hello():
    return 'Hello World'


# Run server
if __name__ == '__main__':
    app.run(debug=True)
