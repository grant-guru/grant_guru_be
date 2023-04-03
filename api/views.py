from django.http import JsonResponse
from .models import User, Grant
from rest_framework import viewsets
from rest_framework.response import Response
from api.serializers import UserSerializer, GrantSerializer

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def list(self, request):
    response = { "data": UserSerializer(self.queryset, many=True).data }
    #return JsonResponse(response, safe=False)
    return Response(response)
  
  def retrieve(self, request, pk=None):
    instance = self.get_object()
    response = { "data": UserSerializer(instance, many=False).data }
    # return JsonResponse(response, safe=False)
    return Response(response)

class GrantViewSet(viewsets.ModelViewSet):
  queryset = Grant.objects.all()
  serializer_class = GrantSerializer

  def list(self, request):
    response = {"data": GrantSerializer(self.queryset, many=True).data }
    return JsonResponse(response, safe=False)
  
