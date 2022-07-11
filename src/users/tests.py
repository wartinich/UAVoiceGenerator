from users.models import User
from django.test import TestCase
from django.urls import reverse


class SignUpTest(TestCase):
    def setUp(self) -> None:
        self.email = 'kolpk@gmail.com'
        self.username = 'kolpk'
        self.password = 'secret'

    def test_signup_url(self):
        response = self.client.get('/sign_up/')
        self.assertEqual(response.status_code, 200)

    def test_signup_form(self):
        response = self.client.post('/sign_up/', data={
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password
        })
        self.assertEqual(response.status_code, 200)


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'test',
            'password': 'secret'
        }
        User.objects.create_user(**self.credentials)

    def test_login_url(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_form(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)


class LogOutTest(TestCase):
    def test_logout_url(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 200)

    def test_logout_form(self):
        response = self.client.post('/logout/')
        self.assertEqual(response.status_code, 200)


class ResetPasswordTest(TestCase):
    def test_reset_password_url(self):
        response = self.client.get('/password-reset/')
        self.assertEqual(response.status_code, 200)

    def test_reset_password_form(self):
        response = self.client.post('/password-reset/', data={'email': 'kolpk@gmail.com'})
        self.assertEqual(response.status_code, 302)

    def test_reset_password_done(self):
        response = self.client.get('/password-reset/done/')
        self.assertEqual(response.status_code, 200)

    def test_reset_password_complete(self):
        response = self.client.get('/password-reset-complete/')
        self.assertEqual(response.status_code, 200)
