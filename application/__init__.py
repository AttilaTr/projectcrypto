from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@34.105.204.236/projectcrypto'
app.config['SECRET_KEY'] = 'epaosidhsauidmascy4238lmgwe678d'
db = SQLAlchemy(app)

from application import routes