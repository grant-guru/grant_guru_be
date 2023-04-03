from .models import Grant, User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
  
class GrantSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Grant
    fields = '__all__' 
