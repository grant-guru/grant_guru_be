from .models import User, Grant
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from api.serializers import UserSerializer, GrantSerializer
from django.http import JsonResponse, HttpResponse
# from django.views.decorators.csrf import csrf_exempt

class GrantViewSet(viewsets.ModelViewSet):
  queryset = Grant.objects.all()
  serializer_class = GrantSerializer

# @csrf_exempt
def grant_list(request):
  # import ipdb; ipdb.set_trace()
  if request.method == 'GET':
    grants = Grant.objects.all()
    serializer = GrantSerializer(grants, many=True)
    return JsonResponse(serializer.data, safe=False)

def grant_detail(request, pk):
  try:
    grant = Grant.objects.get(pk=pk)
    serializer = GrantSerializer(grant, many=False)
    return JsonResponse(serializer.data, safe=False)

  except Grant.DoesNotExist:
    return HttpResponse(status=404)
  
def favorite(request, pk):
  try:
    user = Grant.objects.get(pk=pk)
    favorites = user.grants.all()
    serializer = GrantSerializer(favorites, many=True)
    return JsonResponse(serializer.data, safe=False)
  except Grant.DoesNotExist:
    return HttpResponse(status=404)
  
def favorite_create(request, pk_user, pk_grant):
  # TODO: error handling
  user = User.objects.get(pk=pk_user)
  favorite = Grant.objects.get(pk=pk_grant)
  if request.method == 'POST':
    print("create a favorite conditional branch")
    user.grants.add(favorite)
    serializer = GrantSerializer(favorite, many=False)
    return JsonResponse(serializer.data, safe=False), HttpResponse(status=201)
  elif request.method == 'DELETE':
    print("delete a favorite conditional branch")
    user.favorites.remove(favorite)
    # n HttpResponseRedirect after s

  # except 

class UserViewSet(viewsets.ModelViewSet):
  # import ipdb; ipdb.set_trace()
  queryset = User.objects.all()
  serializer_class = UserSerializer


# def user(request):
  # user = User.objects.filter(id=request)
  # serializer = UserSerializer(user, many=False)
  # return JsonResponse(serializer.data)
  # get the user
  # serialize it
  # return json

