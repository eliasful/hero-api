from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import filters
from hero.models import Hero
from .serializers import HeroSerializer


class HeroViewSet(ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


    @action(methods=['get'], detail=False)
    def favorites(self, request):
        favorites = Hero.objects.filter(favorite=True)
        serializer = HeroSerializer(favorites, many=True)
        return Response(serializer.data)
