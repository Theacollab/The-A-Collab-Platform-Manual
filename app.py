from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///collab.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template("index.html")

# Initialize Database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
