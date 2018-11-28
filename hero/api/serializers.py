from rest_framework.serializers import ModelSerializer
from hero.models import Hero


class HeroSerializer(ModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'description', 'photo')
