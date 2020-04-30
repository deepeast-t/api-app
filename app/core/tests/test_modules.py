from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_crete_user_with_email_succesful(self):
        '''Test create user with an email is successful'''
        email = 'test@debdeb.pl'
        password = 'passpass'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'test@TESTES.PL'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test if """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123pass')

    def test_create_new_super_user(self):
        """CReate super user test"""

        user = get_user_model().objects.create_superuser(
            'test@testest.pl',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)