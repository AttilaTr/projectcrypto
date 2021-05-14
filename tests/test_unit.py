import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Crypto, Articles

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
        WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        db.create_all()
        test_crypto = Crypto(name='IOTA', acronym='MIOTA', description='Progressive crypto', valueusd=720)
        db.session.add(test_crypto)
        db.session.commit()
        test_articles = Articles(title='Smart contact protocol?', author='cointelegraph.com', topic='New service for IOTA', link='https://cointelegraph.com/news/iota-releases-smart-contracts-protocol', crypto_id=test_crypto.id)
        db.session.add(test_articles)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_create_get(self):
        response = self.client.get(url_for('createcrypto'))
        self.assertEqual(response.status_code, 200)

    def test_create_get(self):
        response = self.client.get(url_for('createarticles'))
        self.assertEqual(response.status_code, 200)

    def test_update_get(self):
        response = self.client.get(url_for('updatecrypto', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for('deletecrypto', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for('deletearticles', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

class TestRead(TestBase):
    def test_read_home(self):
        response = self.client.get(url_for('home'))
        self.assertIn(b'CryptoArticles', response.data)

class TestCreateC(TestBase):
    def test_create_crypto(self):
        response = self.client.post(
            url_for('createcrypto'),
            data=dict(name='Bitcoin', acronym='BTC', description='Elons favourite', valueusd=55000),
            follow_redirects=True
        )
        self.assertIn(b'Bitcoin', response.data)

class TestCreateA(TestBase):
    def test_create_articles(self):
        response = self.client.post(
            url_for('createarticles'),
            data=dict(title='Affects on the economy', author='bbc.com', topic='Interesting', link='bbc.com', crypto_id=1),
            follow_redirects=True
        )
        self.assertIn(b'Affects on the economy', response.data)

class TestUpdate(TestBase):
    def test_update_crypto(self):
        response = self.client.post(
            url_for('updatecrypto', id=1),
            data=dict(description='Update a Crypto'),
            follow_redirects=True
        )
        self.assertIn(b'Update a Crypto', response.data)

class TestDeleteC(TestBase):
    def test_delete_crypto(self):
        response = self.client.post(
            url_for('deletecrypto', id=1),
            follow_redirects=True
        )
        self.assertNotIn(b'Delete a Crypto', response.data)

class TestDeleteA(TestBase):
    def test_delete_articles(self):
        response = self.client.post(
            url_for('deletearticles', id=1),
            follow_redirects=True
        )
        self.assertNotIn(b'Delete an Article', response.data)

