from django.urls import path

from detect_api.views import ThemeDetail, ThemeList

urlpatterns = [
    path('<int:pk>/', ThemeDetail.as_view()),
    path('', ThemeList.as_view()),
]
