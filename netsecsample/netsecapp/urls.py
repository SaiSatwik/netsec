# api/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from netsecapp import views


urlpatterns = [
    path('', views.DeviceIpList.as_view()),
    path('<int:pk>/', views.DeviceIpDetail.as_view()),
]
