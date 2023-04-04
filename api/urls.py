from django.urls import path
from api import views

urlpatterns = [
    path('users/<int:pk_user>/scholarships/<int:pk_grant>', views.favorite_create),
    path('scholarships/', views.GrantViewSet.list),
    path('scholarships/<int:pk>/', views.GrantViewSet.retrieve),
    path('users/<int:pk_user>/favorites', views.favorite),
]