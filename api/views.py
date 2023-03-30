from .models import User, Grant
from rest_framework import viewsets
from api.serializers import UserSerializer, GrantSerializer

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class GrantViewSet(viewsets.ModelViewSet):
  queryset = Grant.objects.all()
  serializer_class = GrantSerializer