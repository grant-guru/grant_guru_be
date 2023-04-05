from django.urls import path
from api import views

urlpatterns = [
    path('users/<int:pk_user>/scholarships/<int:pk_grant>', views.GrantViewSet.favorite_create),
    path('users/<int:pk_user>/favorites/', views.GrantViewSet.favorites),
]