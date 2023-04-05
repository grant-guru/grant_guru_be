from django.urls import path
from api import views

urlpatterns = [
    path('users/<int:pk_user>/scholarships/<int:pk_grant>', views.FavoriteViewSet.as_view({
      'post': 'create',
      'delete': 'destroy',
    })),
    path('users/<int:pk_user>/favorites/', views.FavoriteViewSet.as_view({'get': 'list',})),
]