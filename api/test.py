from django.test import TestCase
from .models import Grant, User

class GrantModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a Grant object for testing
        Grant.objects.create(
            title='Test Grant',
            organization='Test Organization',
            description='This is a test grant',
            amount=1000,
            deadline='2023-05-01',
            education='College',
            state='California',
            ethnicity='Asian',
            women=True,
            lgbt=False,
            veteran=False,
            immigrant=True,
            url='http://testgrant.com',
            image_url='http://testgrant.com/image.jpg'
        )

    def test_title_label(self):
        grant = Grant.objects.get(id=1)
        field_label = grant._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_object_name_is_title(self):
        grant = Grant.objects.get(id=1)
        expected_object_name = grant.title
        self.assertEqual(expected_object_name, str(grant))


class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a User object for testing
        user = User.objects.create(
            first_name='Test',
            last_name='User',
            image_url='http://testuser.com/image.jpg',
        )
        grant = Grant.objects.create(
            title='Test Grant',
            organization='Test Organization',
            description='This is a test grant',
            amount=1000,
            deadline='2023-05-01',
            education='College',
            state='California',
            ethnicity='Asian',
            women=True,
            lgbt=False,
            veteran=False,
            immigrant=True,
            url='http://testgrant.com',
            image_url='http://testgrant.com/image.jpg'
        )
        user.grants.add(grant)

    def test_first_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_user_has_grants(self):
        user = User.objects.get(id=1)
        grants = user.grants.all()
        self.assertTrue(grants.exists())

