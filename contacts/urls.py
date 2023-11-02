from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import apiOverview, ContactListApi, ContactCreateApi, ContactUpdateApi, ContactDeleteApi

urlpatterns = [
    path('api-docs/', apiOverview, name='home'),
    path('api-docs/list/', ContactListApi.as_view()),
    path('api-docs/create/', ContactCreateApi.as_view()),
    path('api-docs/update/<int:pk>/', ContactUpdateApi.as_view()),
    path('api-docs/delete/<int:pk>/', ContactDeleteApi.as_view())
]
