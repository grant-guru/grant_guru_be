from django.http import JsonResponse
from .models import User, Grant
from rest_framework import viewsets
from rest_framework.response import Response
# from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
from api.serializers import UserSerializer, GrantSerializer
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def favorite_create(request, pk_user, pk_grant):
  # TODO: error handling
  user = User.objects.get(pk=pk_user)
  favorite = Grant.objects.get(pk=pk_grant)
  if request.method == 'POST':
    user.grants.add(favorite)
    serializer = GrantSerializer(favorite, many=False)
    return Response(serializer.data)
    # TODO: add http status 201
  elif request.method == 'DELETE':
    user.grants.remove(favorite)

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def list(self, request):
    serializer = UserSerializer(self.queryset, many=True)
    return Response(serializer.data)
  
  def retrieve(self, request, pk=None):
    instance = self.get_object()
    serializer = UserSerializer(instance, many=False)
    return Response(serializer.data)
  
  @action(detail=True, methods=['get'])
  def favorites(self, request, pk=None):
    user = self.get_object()
    favorites = user.grants.all()
    serializer = GrantSerializer(favorites, many=True)
    return Response(serializer.data)


class GrantViewSet(viewsets.ModelViewSet):
  queryset = Grant.objects.all()
  serializer_class = GrantSerializer

  def list(self, request):
    education = request.GET.get('education','')
    gender = request.GET.get('gender','')
    state = request.GET.get('state','')
    lgbt = request.GET.get('lgbt','')
    veteran = request.GET.get('veteran','')
    immigrant = request.GET.get('immigrant','')
    unfiltered_ethnicity = request.GET.get('ethnicity','')
    
    q = {}

    if education != '':
      q.update({'education': education})

    if gender != '':
      q.update({'gender': gender})

    if state != '':
      q.update({'state': state})

    if lgbt != '':
      q.update({'lgbt': lgbt})

    if unfiltered_ethnicity != '':
      ethnicity = sorted(unfiltered_ethnicity.replace('[','').replace(']','').split(','))
      q.update({'ethnicity': ethnicity})
    
    if veteran != '':
      q.update({'veteran': veteran})

    if immigrant != '':
      q.update({'immigrant': immigrant})
    
    grants = Grant.objects.filter(**q)
    serializer = GrantSerializer(grants, many=True)
    return Response(serializer.data)
  
  def retrieve(self, request, pk=None):
    instance = self.get_object()
    serializer = GrantSerializer(instance, many=False)
    return Response(serializer.data)
  

