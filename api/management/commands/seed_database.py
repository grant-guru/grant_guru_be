from django.core.management.base import BaseCommand
from api.tests.factories import UserFactory, GrantFactory

class Command(BaseCommand):
  def handle(self, *args, **options):
    UserFactory.create_batch(8)
    GrantFactory.create_batch(100)