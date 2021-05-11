from application import db

class Crypto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    acronym = db.Column(db.String(15), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    valueusd = db.Column(db.Integer, nullable=False)
    articles = db.relationship('Articles', backref='crypto')
    
class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    topic = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(100), nullable=False)
    crypto_id = db.Column(db.Integer, db.ForeignKey('crypto.id'), nullable=False)