from django.core.management.base import BaseCommand
from api.models import User
from api.tests.factories import UserFactory, GrantFactory

class Command(BaseCommand):
  def handle(self, *args, **options):
    User.objects.create(first_name = 'Drew', last_name = 'Layton')
    User.objects.create(first_name = 'Kaylah Rose', last_name = 'Mitchell')
    User.objects.create(first_name = 'Sergio', last_name = 'Azcona')
    User.objects.create(first_name = 'Matisse', last_name = 'Mallette')
    User.objects.create(first_name = 'Keenan', last_name = 'Southall')
    User.objects.create(first_name = 'Reid', last_name = 'Poole')
    User.objects.create(first_name = 'Jocelle', last_name = 'Bautista')
    User.objects.create(first_name = 'Adam', last_name = 'Hughes')
    GrantFactory.create_batch(100)