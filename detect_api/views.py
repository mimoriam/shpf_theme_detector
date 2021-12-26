from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import ThemeModel
from .serializers import ThemeSerializer
from django.http import Http404
from rest_framework import status
from django.shortcuts import get_object_or_404

import requests
import re


# Create your views here.

class ThemeList(generics.ListAPIView):
    queryset = ThemeModel.objects.all()
    serializer_class = ThemeSerializer

    def post(self, request):
        serializer = ThemeSerializer(data=request.data)

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
        theme_name_result = result.group(1)
        print(result.group(1))

        # model_f2 = ThemeModel.objects.all()
        # model_f2_update = model_f2.get(theme_name=theme_name_result)
        # print(model_f2_update)
        # model_f2_update.theme_name = theme_name_result
        # model_f2_update.save()

        # model_f = ThemeModel.objects.get(pk=1)
        # model_f.theme_name = result.group(1)
        # model_f.save()

        # print(model_f.theme_name)
        # model_f.theme_name = result.group(1)
        # model_f.save(['theme_name'])

        # return Response(data=result.group(1))

        # if serializer.is_valid():
        #     theme_url2 = serializer.validated_data['theme_url']
        #     print(theme_url2)
        #     obj, created = ThemeModel.objects.get_or_create(theme_url=theme_url2,
        #                                                     defaults=serializer.validated_data)
        #     if not created:
        #         serializer.save(theme_url=theme_url2)
        #         return Response(serializer.data, status=status.HTTP_201_CREATED)
        #     else:
        #         return Response(status=status.HTTP_409_CONFLICT)

        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # model = get_object_or_404(ThemeModel, pk=pk)
        # data =

        if serializer.is_valid():
            # serializer.save()
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(data=result.group(1))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ThemeDetail(generics.RetrieveDestroyAPIView):
    queryset = ThemeModel.objects.all()
    serializer_class = ThemeSerializer
