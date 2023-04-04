from django.urls import path
from api import views

urlpatterns = [
    path('users/<int:pk_user>/scholarships/<int:pk_grant>', views.favorite_create),
]