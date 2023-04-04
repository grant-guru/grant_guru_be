from django.http import JsonResponse
from .models import User, Grant
from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework.parsers import JSONParser
from api.serializers import UserSerializer, GrantSerializer
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def list(self, request):
    response = { "data": UserSerializer(self.queryset, many=True).data }
    return JsonResponse(response, safe=False)
    # return Response(response)
  
  def retrieve(self, request, pk=None):
    instance = self.get_object()
    response = { "data": UserSerializer(instance, many=False).data }
    return JsonResponse(response, safe=False)
    # return Response(response)

class GrantViewSet(viewsets.ModelViewSet):
  queryset = Grant.objects.all()
  serializer_class = GrantSerializer

  def list(self, request):
    response = {"data": GrantSerializer(self.queryset, many=True).data }
    return JsonResponse(response, safe=False)
    # return Response(response)
  
  def retrieve(self, request):
    instance = self.get_object()
    response = { "data": GrantSerializer(instance, many=False).data }
    return JsonResponse(response, safe=False)
    # return Response(response, safe=False)

def favorite(request, pk):
  try:
    user = Grant.objects.get(pk=pk)
    favorites = user.grants.all()
    serializer = GrantSerializer(favorites, many=True)
    return JsonResponse(serializer.data, safe=False)
  except Grant.DoesNotExist:
    return HttpResponse(status=404)
  
@csrf_exempt
def favorite_create(request, pk_user, pk_grant):
  # TODO: error handling
  user = User.objects.get(pk=pk_user)
  favorite = Grant.objects.get(pk=pk_grant)
  if request.method == 'POST':
    favorite.users.add(user)
    serializer = GrantSerializer(favorite, many=False)
    return JsonResponse(serializer.data)
    # TODO: add http status 201
  elif request.method == 'DELETE':
    print("delete a favorite conditional branch")
    user.favorites.remove(favorite)
