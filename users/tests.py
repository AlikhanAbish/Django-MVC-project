from django.test import TestCase
from django.urls import reverse, reverse_lazy
from http import HTTPStatus
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationViewTestCase(TestCase):



    def setUp(self):
        self.path = reverse('users:registration')

    def test_registration_page_loads(self):
        # path = reverse('users:registration')
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Registration')
        self.assertTemplateUsed(response, 'users/registration.html')


    def test_user_registration_success(self):
        form_data = {
            'first_name': 'testuser',
            'last_name': 'testsuname',
            'username': 'testusername',
            'email': 'testuser@test.com',
            'password1': 'strongpass123',
            'password2': 'strongpass123',
        }

        response = self.client.post(self.path, form_data)

        self.assertEqual(response.url, reverse('users:login'))

        self.assertTrue(User.objects.filter(username = 'testusername').exists())

        user = User.objects.get(username = 'testusername')

        self.assertTrue(user.check_password(form_data['password1']))

