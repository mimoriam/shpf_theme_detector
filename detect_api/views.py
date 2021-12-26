from django.shortcuts import render
from rest_framework import generics
from .models import ThemeModel
from .serializers import ThemeSerializer


# Create your views here.

class ThemeList(generics.ListAPIView):
    queryset = ThemeModel.objects.all()
    serializer_class = ThemeSerializer


class ThemeDetail(generics.RetrieveDestroyAPIView):
    queryset = ThemeModel.objects.all()
    serializer_class = ThemeSerializer
