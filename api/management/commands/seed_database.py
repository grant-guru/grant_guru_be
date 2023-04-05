from django.core.management.base import BaseCommand
from api.models import User
from api.tests.factories import UserFactory, GrantFactory

class Command(BaseCommand):
  def handle(self, *args, **options):
    for _ in range(100):
      GrantFactory.create()

    User.objects.create(
      first_name = 'Drew', 
      last_name = 'Layton', 
      image_url = 'https://media.licdn.com/dms/image/D5635AQHEnwpJLXt26Q/profile-framedphoto-shrink_800_800/0/1678064386468?e=1680879600&v=beta&t=p8ZKUqplSskK5g-2phNbRo1UgXLdLMAZ0X_lmdowZfs')
    User.objects.create(
      first_name = 'Kaylah Rose', 
      last_name = 'Mitchell', 
      image_url = 'https://media.licdn.com/dms/image/D5603AQF267qmv4H5LA/profile-displayphoto-shrink_800_800/0/1675731750982?e=1685577600&v=beta&t=j9AGMADYpyBgk6ez01xqivshVOADLvPjGJBs6woSLVQ')
    User.objects.create(
      first_name = 'Sergio', 
      last_name = 'Azcona', 
      image_url = 'https://media.licdn.com/dms/image/C5603AQFg36SHA4Yaow/profile-displayphoto-shrink_800_800/0/1655168145023?e=1685577600&v=beta&t=7HIj5uv3UqIPvspsiIpPDIvJfr0DhNAzVezFZ6SBsTs')
    User.objects.create(
      first_name = 'Matisse', 
      last_name = 'Mallette', 
      image_url = 'https://media.licdn.com/dms/image/C5603AQGZliXUratj0Q/profile-displayphoto-shrink_800_800/0/1663354238434?e=1685577600&v=beta&t=0Tbn6cOH3rp45302bhx2oanUXtrvC1XtDdvmEpScUpw')
    User.objects.create(
      first_name = 'Keenan', 
      last_name = 'Southall', 
      image_url = 'https://media.licdn.com/dms/image/D4E03AQHgAoRoOzOChQ/profile-displayphoto-shrink_800_800/0/1665629022125?e=1685577600&v=beta&t=UmtbW5x5VcrvtDl45ngIvA0f1B9E_hRDH1JDZgHcj3A')
    User.objects.create(
      first_name = 'Reid', 
      last_name = 'Poole', 
      image_url = 'https://media.licdn.com/dms/image/D5635AQF3PxKiLVYhcw/profile-framedphoto-shrink_800_800/0/1679083658885?e=1680883200&v=beta&t=XpcpJSCPzhfxR-RLDg--6CCQHIv6u0BdV7ooCmOs5Jo')
    User.objects.create(
      first_name = 'Jocelle', 
      last_name = 'Bautista', 
      image_url = 'https://media.licdn.com/dms/image/D5635AQEIHVN77x1QAw/profile-framedphoto-shrink_800_800/0/1678550742745?e=1680879600&v=beta&t=ieS0A5xEOTfyWAToumQR3iE9CmfucWFDsx1S1xCqDdo')
    User.objects.create(
      first_name = 'Adam', 
      last_name = 'Hughes', 
      image_url = 'https://media.licdn.com/dms/image/C5603AQHvilQI3AUEMQ/profile-displayphoto-shrink_800_800/0/1609862815851?e=1685577600&v=beta&t=HMl5xDZTacnO-E1fQSgfzhgzCJKMBc3x-pj5LaSZA-M')