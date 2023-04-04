from .models import User, Grant
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from api.serializers import UserSerializer, GrantSerializer
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from rest_framework import DjangoFilterBackend


class GrantViewSet(viewsets.ModelViewSet):
  queryset = Grant.objects.all()
  serializer_class = GrantSerializer
  # filter_backends = [DjangoFilterBackend]

def grant_list(request):
  if request.method == 'GET':
    # filterset_fields = ['education','gender','state','lgbt','ethnicity','veteran','title','immigrant']
    education = request.GET.get('education','')
    veteran = request.GET.get('veteran','')
    title = request.GET.get('title','')
    # grants = Grant.objects.all(lgbt = request.META['HTTP_LGBT'])
  

    q = {}
    if education != '':
      q.update({'education': education})

    if veteran != '':
      q.update({'veteran': veteran})

    if title != '':
      q.update({'title': title})

    grants = Grant.objects.filter(**q)
    import ipdb; ipdb.set_trace()


    # search = query_params(request.META) #Grant._meta.get_fields() - gets the field names in the table
    grants = Grant.objects.filter(title=title)
    # serializer = GrantSerializer(grants, many=True)
    # return JsonResponse(serializer.data, safe=False)
  
  def get_queryset(self):
    import ipdb; ipdb.set_trace()

# def query_params(meta_data):
#     'HTTP_STATE'
    # for k, v in meta_data.items
    #   if i.values()
    #   return i.items()

      
    # "HTTP_STATE"

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
  
@csrf_exempt
def favorite_create(request, pk_user, pk_grant):
  # TODO: error handling
  user = User.objects.get(pk=pk_user)
  favorite = Grant.objects.get(pk=pk_grant)
  if request.method == 'POST':
    # print("create a favorite conditional branch")
    favorite.users.add(user)
    # user.grants.add(favorite)
    serializer = GrantSerializer(favorite, many=False)
    # import ipdb; ipdb.set_trace()
    # return JsonResponse(serializer.data), HttpReponse(status=201)
    return JsonResponse(serializer.data)
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