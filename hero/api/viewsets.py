from rest_framework.viewsets import ModelViewSet
from hero.models import Hero
from .serializers import HeroSerializer


class HeroViewSet(ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
