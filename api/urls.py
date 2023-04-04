from django.urls import path
from api import views

urlpatterns = [
    path('users/<int:pk_user>/scholarships/<int:pk_grant>', views.favorite_create),
    path('scholarships/', views.grant_list),
    path('scholarships/<int:pk>/', views.grant_detail),
    path('users/<int:pk_user>/favorites', views.favorite),
]