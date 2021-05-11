from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@34.105.204.236/projectcrypto'

db = SQLAlchemy(app)

from application import routes