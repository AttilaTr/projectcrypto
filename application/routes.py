from application import app, db
from application.models import Tasks
from application.forms import TaskForm
from flask import render_template, request, redirect

@app.route('/create')
def add():
    new_crypto = Crypto(name = 'Name of crypto', acronym = 'Acronym of crypto', description = 'Descryption of crypto', valueusd = 'Value of crypto in USD')
    db.session.add(new_crypto)
    db.session.commit()
    return 'New cryptocurrency added to database'

@app.route('/read')
def read():
    all_crypto = Crypto.query.all()
    crypto_string = ''
    for crypto in all_crypto:
        crypto_string += '<br>'+ crypto.name
    return crypto_string

@app.route('/update/<name>, <acronym>, <description>, <valueusd>')
def update(name, acronym, description, valueusd):
    first_crypto = Crypto.query.first()
    first_crypto.name = name
    first_crypto.acronym = acronym
    first_crypto.name = description
    first_crypto.name = valueusd
    db.session.commit()
    return first_crypto.name

@app.route('/delete/')
def delete():
    crypto_to_delete = Crypto.query.first()
    db.session.delete(crypto_to_delete)
    db.session.commit()