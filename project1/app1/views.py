from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app1.models import Anime
from app1.serializers import Anime_serializer


# Create your views here.

class Anime1(APIView):
    def get(self, request):
        Animes = Anime.objects.all()
        Anime_serializer_data = Anime_serializer(Animes, many=True)
        return Response(data=Anime_serializer_data.data)
    
    

    def post(self, request):
        Anime_serializer_data = Anime_serializer(data=request.data)
        if Anime_serializer_data.is_valid():
            Anime_serializer_data.save()
            return Response(data=Anime_serializer_data.data)
        return Response(data=Anime_serializer_data.errors)

class Anime_item(APIView):
    def get(self,request,pk):
        obj=get_object_or_404(Anime,pk=pk)
        obj_serializer=Anime_serializer(obj)
        return Response(data=obj_serializer.data,status= status.HTTP_200_OK)

    def put(self,request,pk):
        obj=get_object_or_404(Anime,pk=pk)
        obj_serializer=Anime_serializer(data=request.data,instance=obj)
        if obj_serializer.is_valid():
            obj_serializer.save()
            return Response(data=obj_serializer.data,status=status.HTTP_200_OK)
        return Response(data=obj_serializer.errors,status=status.HTTP_205_RESET_CONTENT)

    def patch(self,request,pk):
        obj=get_object_or_404(Anime,pk=pk)
        obj_serializer=Anime_serializer(data=request.data,instance=obj,partial=True)
        if obj_serializer.is_valid():
            obj_serializer.save()
            return Response(data=obj_serializer.data,status=status.HTTP_200_OK)
        return Response(data=obj_serializer.errors,status=status.HTTP_205_RESET_CONTENT)

    def delete(self,request,pk):
        obj=get_object_or_404(Anime,pk=pk)
        obj.delete()
        return Response(data=None, status=status.HTTP_204_NO_CONTENT)

# git change pratuce 1





