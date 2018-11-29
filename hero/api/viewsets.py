from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from hero.models import Hero
from .serializers import HeroSerializer


class HeroFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')
    favorite = filters.CharFilter(field_name="favorite")
    
    
class Meta:
    model = Hero
    fields = ['name', 'favorite']
 

class HeroViewSet(ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = HeroFilter
    ordering_fields = ('id',)
    
    
    @action(methods=['get'], detail=False)
    def favorites(self, request):
        favorites = Hero.objects.filter(favorite=True)
        serializer = HeroSerializer(favorites, many=True)
        return Response(serializer.data)
