from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

@app.route('/')
def hello():
    return 'Hello, this is a Flask server with SQLAlchemy!'

@app.route('/api/items')
def get_items():
    items = Item.query.all()
    data = [{'name': item.name, 'description': item.description} for item in items]
    return jsonify(data)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
