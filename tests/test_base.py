"""Flask tests."""

from flask_testing import TestCase
from flask import current_app

from main import app


class MainTest(TestCase):
    """Main test case."""

    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        return app
    
    def test_app_exists(self):
        self.assertIsNotNone(current_app)        

    def test_app_in_testing_mode(self):
        self.assertTrue(current_app.config['TESTING'])
    
    def test_index_redirects(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/hello')
    
    def test_hello_get(self):
        response = self.client.get('/hello')
        self.assert_200(response)
    
    def test_hello_post(self):
        fake_form = {
            'username': 'fake',
            'password': 'fake-password'
        }
        response = self.client.post('/hello', data=fake_form)
        self.assertRedirects(response, '/')
