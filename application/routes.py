from application import app, db
from application.models import Crypto, Articles
from application.forms import CryptoForm, ArticlesForm
from flask import render_template, request, redirect, url_for

@app.route('/')
@app.route('/home')
def home():
    render_template('index.html', title='Home')


@app.route('/createcrypto', methods=['GET', 'POST'])
def createcrypto():
    form = CryptoForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_crypto = Crypto(name=form.name.data)
            db.session.add(new_crypto)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('createcrypto.html', title='Create a cryptocurrency', form=form)

@app.route('/createarticles', methods=['GET', 'POST'])
def createarticles():
    form = ArticlesForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_article = Articles(title=form.article.data)
            db.session.add(new_article)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('createarticles.html', title='New Article entry', form=form)

@app.route('/deletecrypto', methods=['GET', 'DELETE'])
def deletecrypto():
    form = CryptoForm()
    crypto = Crypto.query.filter_by(id=id).first()
    if request.method == 'DELETE':
        if form.validate_on_submit1():
            db.session.delete(crypto)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('deletecrypto.html', title='Delete Crypto', form=form)

@app.route('/deletearticle', methods=['GET', 'DELETE'])
def deletearticle():
    form = ArticlesForm()
    article = Articles.query.filter_by(id=id).first()
    if request.method == 'DELETE':
        if form.validate_on_submit1():
            db.session.delete(article)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('deletearticle.html', title='Delete Article', form=form)

@app.route('/updatecrypto', methods=['GET', 'PUT'])
def update():
    form = CryptoForm()
    crypto = Crypto.query.filter_by(id=id).first()
    if request.method == 'PUT':
        if form.validate_on_submit2():
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('updatecrypto.html', title='Update Crypto', form=form)