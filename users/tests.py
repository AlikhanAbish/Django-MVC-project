from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, reverse_lazy

User = get_user_model()


class UserRegistrationViewTestCase(TestCase):

    def setUp(self):
        self.form_data = {
            'first_name': 'testuser',
            'last_name': 'testsuname',
            'username': 'testusername',
            'email': 'testuser@test.com',
            'password1': 'strongpass123',
            'password2': 'strongpass123',
        }
        self.path = reverse('users:registration')


    def test_registration_page_loads(self):
        # path = reverse('users:registration')
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Registration')
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_user_registration_success(self):

        response = self.client.post(self.path, self.form_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response.url, reverse('users:login'))
        user = User.objects.get(username='testusername')
        self.assertTrue(User.objects.filter(username='testusername').exists())
        self.assertTrue(user.check_password(self.form_data['password1']))

    def test_user_registration_post_error(self):
        User.objects.create(username=self.form_data['username'])
        response = self.client.post(self.path, self.form_data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Пользователь с таким именем уже существует.', html=True)