from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import ThemeModel
from .serializers import ThemeSerializer

import requests
import re


# Create your views here.

class ThemeList(generics.ListAPIView):
    queryset = ThemeModel.objects.all()
    serializer_class = ThemeSerializer

    def post(self, request):
        post_data = request.data
        # post_data_dict = post_data.dict()
        post_data_url = post_data.__getitem__('theme_url')

        # Umair's script starts here:
        url = post_data_url
        req = requests.get(url, 'html.parser')
        cSource = req.text
        # result = re.search("""window.BOOMR.themeName = "(.*)"; window.BOOMR.themeVersion""", cSource)
        result = re.search("""window.BOOMR.themeName = "(.*)";""", cSource)
        # result2 = re.search("""window.BOOMR.themeVersion""", cSource)
        print(result.group(1))

        return Response(data=result.group(1))


class ThemeDetail(generics.RetrieveDestroyAPIView):
    queryset = ThemeModel.objects.all()
    serializer_class = ThemeSerializer
