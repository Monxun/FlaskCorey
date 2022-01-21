from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  #__main__
app.config['SECRET_KEY'] = '74c03dfb30a2c32a712d27394e9537c8'
# >>> import secrets
# >>> secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from app import routes