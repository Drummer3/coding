from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'

db = SQLAlchemy(app)

class Course(db.Model):
  id = db.Column(db.Integer,primary_key = True)
  Name = db.Column(db.String(40))
  Image = db.Column(db.Text)
  Price = db.Column(db.Integer)
@app.route('/')
def course_list():  
  courses = Course.query.all()
  return render_template('index.html',courses = courses)

@app.route('/cart')
def cart_page():
  return render_template('cart.html')

@app.route('/add-cart')
def add_cart():
  print('Here must be item name')
  return render_template('index.html')

@app.route('/about-us')
def about_us():
  return render_template('about-us.html')

@app.route('/contacts')
def contacts_page():
  return render_template('contacts.html')

app.run(host='localhost', port=80)