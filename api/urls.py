from django.urls import path
from api import views

urlpatterns = [
    path('scholarships/', views.grant_list),
    path('grants/<int:pk/', views.grant_detail),
    path('users/<int:pk_user/favorites', views.favorite),
    path('users/<int:pk_user/scholarships/<int:pk_grant', views.favorite_create),
]