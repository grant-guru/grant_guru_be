from django.http import JsonResponse
from .models import User, Grant
from rest_framework import viewsets
from rest_framework.response import Response
# from rest_framework.parsers import JSONParser
from rest_framework.decorators import action, api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from api.serializers import UserSerializer, GrantSerializer
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def list(self, request):
    serializer = UserSerializer(self.queryset, many=True)
    return Response(serializer.data)
  
  def retrieve(self, request, pk=None):
    instance = self.get_object()
    serializer = UserSerializer(instance, many=False)
    # import ipdb; ipdb.set_trace()
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
    
    query = {'women': False}

    if education != '':
      query.update({'education': education})

    if gender == 'Woman':
      del query['women']

    if state != '':
      query.update({'state': state})

    if lgbt != '':
      query.update({'lgbt': lgbt})

    if unfiltered_ethnicity != '':
      filtered_ethnicity = unfiltered_ethnicity.replace('[','').replace(']','').split(',')
      query.update({'ethnicity__in': filtered_ethnicity})
    
    if veteran != '':
      query.update({'veteran': veteran})

    if immigrant != '':
      query.update({'immigrant': immigrant})
    
    grants = Grant.objects.filter(**query)
    serializer = GrantSerializer(grants, many=True)
    return Response(serializer.data)
  
  def retrieve(self, request, pk=None):
    instance = self.get_object()
    serializer = GrantSerializer(instance, many=False)
    return Response(serializer.data)

class FavoriteViewSet(viewsets.ModelViewSet):
  queryset = Grant.objects.all()
  serializer_class = GrantSerializer

  # @api_view(('GET',))
  # @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
  # @action(detail=True, methods=['get'])
  def list(self, request, pk_user=None):
    user = User.objects.get(pk=pk_user)
    grants = user.grants.all()
    serializer = GrantSerializer(grants, many=True)
    return Response(serializer.data)

  @csrf_exempt
  # @api_view(('post',))
  def create(self, request, pk_user, pk_grant):
    # TODO: error handling
    user = User.objects.get(pk=pk_user)
    favorite = Grant.objects.get(pk=pk_grant)
    user.grants.add(favorite)
    serializer = GrantSerializer(favorite, many=False)
    return Response(serializer.data)

  # @csrf_exempt
  # def destroy(self, request, pk_user, pk_grant):
  #   # TODO: add http status 201
  #   user = User.objects.get(pk=pk_user)
  #   favorite = Grant.objects.get(pk=pk_grant)
  #   user.grants.remove(favorite)
  #   serializer = GrantSerializer(favorite, many=False)
  #   return Response(serializer.data)