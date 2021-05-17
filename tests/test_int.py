from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for

from application import app, db
from application.models import Crypto, Articles

class TestBase(LiveServerTestCase):
    TEST_PORT = 5050

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            LIVESERVER_PORT=self.TEST_PORT,

            DEBUG=True,
            TESTING=True
        )

        return app

def setUp(self):

    chrome_options = webdriver.chrome.options.Options()
    chrome_options.add_argument('--headless')

    self.driver = webdriver.Chrome(options=chrome_options)

    db.create_all()

    self.driver.get(f'http://localhost:{self.TEST_PORT}')

def tearDown(self):
    self.driver.quit()

    db.drop_all()

def test_server_is_up_and_running(self):
    response = urlopen(f'http://localhost:{self.TEST_PORT}')
    self.assertEqual(response.code, 200)

class TestAdd(TestBase):
    TEST_CASES = 'Cardano', 'ADA', 'New hope', 4500

    def submit_input(self, case):
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys(case)
        self.driver.find_element_by_xpath('//*[@id="acronym"]').send_keys(case)
        self.driver.find_element_by_xpath('//*[@id="description"]').send_keys(case)
        self.driver.find_element_by_xpath('//*[@id="valueusd"]').send_keys(case)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()