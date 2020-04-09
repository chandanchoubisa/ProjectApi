from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

def sample_user(email='test@gmail.com',password='testpass'):
    """Create a smaple user"""
    return get_user_model().objects.create_user(email,password)



class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test Creating a new user with an email is successful"""
        email = 'test@chandan.com'
        password = 'Chandan'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_normalize_email_of_user(self):
        """Test for Normalize email in lower case"""
        email = "test@CHANDAN.COM"
        user = get_user_model().objects.create_user(email, 'Chandan')

        self.assertEqual(user.email,email.lower())


    def test_user_invalid_email(self):
        """Test for invalid email raises Value error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')


    def test_create_new_superuser(self):
        """For Creating new Superuser"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """test the tag string representation"""
        tag = models.Tag.objects.create(
            user = sample_user(),
            name = 'Vegan'
        )
        self.assertEqual(str(tag),tag.name)

