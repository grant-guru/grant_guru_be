from pytest_factoryboy import register
from .factories import UserFactory, GrantFactory

register(UserFactory)
register(GrantFactory)