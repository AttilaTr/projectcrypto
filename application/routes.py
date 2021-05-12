from application import app, db
from application.models import Crypto, Articles
from application.forms import CryptoForm, ArticlesForm
from flask import render_template, request, redirect, url_for

@app.route('/')
@app.route('/home')
def home():
all_crypto = Crypto.query.all()
    output = ""
    return render_template('index.html', title='Home', all_crypto=all_crypto)


@app.route('/create', methods=['GET', 'POST'])
def create():
    form = CryptoForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_crypto = Crypto(name=form.name.data)
            db.session.add(new_crypto)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('add.html', title='Create a cryptocurrency', form=form)

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