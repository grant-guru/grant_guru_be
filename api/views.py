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
  if request.method == 'GET':
    grants = Grant.objects.all()
    serializer = GrantSerializer(grants, many=True)
    return JsonResponse(serializer.data, safe=False)

def grant_detail(request, pk):
  try:
    grant = Grant.objects.get(pk=pk)
  except Grant.DoesNotExist:
    return HttpResponse(status=404)
  

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

