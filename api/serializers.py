from .models import Grant, User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

  # id = serializers.IntegerField(read_only=True)
  # first_name = serializers.CharField(required=True, max_length=100)
  # last_name = serializers.CharField(required=True, max_length=100)
  
  def create(self, validated_data):
    return User.objects.create(**validated_data)

class GrantSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Grant
    fields = '__all__' 
