from django.urls import path
from api import views

urlpatterns = [
    path('api/v1/users/<int:pk_user>/scholarships/<int:pk_grant>', views.favorite_create),
    path('api/v1/scholarships/', views.grant_list),
    path('api/v1/scholarships/<int:pk>/', views.grant_detail),
    path('api/v1/users/<int:pk_user>/favorites', views.favorite),
]