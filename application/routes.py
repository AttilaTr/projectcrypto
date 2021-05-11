from application import app, db
from flask import render_template

@app.route('/home/<word>')
def home(word):
    if word == 'Crypto':
        return 'This will be the Crypto db'
    if word == 'Articles':
        return 'This will be the Article db'
    else:
        return 'Have a good day'

