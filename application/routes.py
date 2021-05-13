from application import app, db
from application.models import Crypto, Articles
from application.forms import CryptoForm, ArticlesForm
from flask import render_template, request, redirect, url_for

@app.route('/')
@app.route('/home')
def home():
    all_articles = Articles.query.all()
    all_crypto = Crypto.query.all()
    return render_template('index.html', title='Home', all_crypto=all_crypto, all_articles=all_articles)


@app.route('/createcrypto', methods=['GET', 'POST'])
def createcrypto():
    form = CryptoForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_crypto = Crypto(name=form.name.data, acronym=form.acronym.data, description=form.description.data, valueusd=form.valueusd.data)
            db.session.add(new_crypto)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('createcrypto.html', title='Create a cryptocurrency', form=form)

@app.route('/createarticles', methods=['GET', 'POST'])
def createarticles():
    form = ArticlesForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            cryptoid = Crypto.query.filter_by(acronym=form.cryptoacronym.data).first().id
            new_article = Articles(title=form.title.data, author=form.author.data, topic=form.topic.data, link=form.link.data, crypto_id=cryptoid)
            db.session.add(new_article)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('createarticles.html', title='New Article entry', form=form)

@app.route('/deletecrypto/<int:id>', methods=['GET', 'DELETE'])
def deletecrypto(id):
    crypto = Crypto.query.filter_by(id=id).first()
    db.session.delete(crypto)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/deletearticles/<int:id>', methods=['GET', 'DELETE'])
def deletearticles(id):
    articles = Articles.query.filter_by(id=id).first()
    db.session.delete(articles)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/updatecrypto/<int:id>', methods=['GET', 'POST'])
def updatecrypto(id):
    form = CryptoForm()
    crypto = Crypto.query.filter_by(id=id).first()
    if request.method == 'POST':
        if form.validate_on_submit():
            crypto.name = form.name.data
            crypto.acronym = form.acronym.data
            crypto.description = form.description.data
            crypto.valueusd = form.valueusd.data
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('updatecrypto.html', title='Update Crypto', form=form)