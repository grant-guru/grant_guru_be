from django.test import TestCase
from api.models import User, Grant
from api.tests.factories import UserFactory, GrantFactory
from datetime import date

class UserTests(TestCase):
  def test_user_data_types(self):
    user = UserFactory()

    assert isinstance(user, User)
    assert isinstance(user.first_name, str)
    assert isinstance(user.last_name, str)

class GrantTests(TestCase):
  def test_grant_data_types(self):
    grant = GrantFactory()

    assert isinstance(grant, Grant)
    assert isinstance(grant.title, str)
    assert isinstance(grant.organization, str)
    assert isinstance(grant.amount, int)
    assert isinstance(grant.description, str)
    assert isinstance(grant.deadline, date)
    assert isinstance(grant.education, str)
    assert isinstance(grant.state, str)
    assert isinstance(grant.ethnicity, str)
    assert isinstance(grant.women, bool)
    assert isinstance(grant.lgbt, bool)
    assert isinstance(grant.veteran, bool)
    assert isinstance(grant.immigrant, bool)
    assert isinstance(grant.url, str)
    assert isinstance(grant.image_url, str)