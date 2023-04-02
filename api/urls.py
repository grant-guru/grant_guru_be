from django.urls import path
from api import views

urlpatterns = [
    path('grants/', views.grant_list),
    path('grants/<int:pk/', views.grant_detail),
]