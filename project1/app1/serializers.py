from rest_framework import  serializers

from app1.models import Anime


class Anime_serializer(serializers.ModelSerializer):
    class Meta:
        model=Anime
        fields="__all__"



