from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///find_books.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    location_State = db.Column(db.String(60), nullable=False)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    hint = db.Column(db.String(1000), nullable=False)
    location_State = db.Column(db.String(60), nullable=False)
    location_City = db.Column(db.String(60), nullable=False)
    code_words = db.Column(db.String(30), nullable=False)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')
@app.route('/about')
def about_page():
    return render_template('about.html')
@app.route('/find_books')
def find_books():
    return render_template('find_books.html')

if __name__ == "__main__":
     app.run()