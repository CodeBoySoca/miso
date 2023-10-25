from flask import Flask, render_template
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os
import datetime

load_dotenv('.env')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)

class Reservations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=True)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.Time, nullable=False)
    notification_status = db.Column(db.Boolean, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reservations')
def reservation():
    pass

@app.route('/events')
def events():
    pass

@app.route('/menu')
def menu():
    pass

@app.route('/mail')
def mail():
    pass



if __name__ == '__main__':
    app.run()