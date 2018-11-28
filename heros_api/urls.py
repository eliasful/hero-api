from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from hero.api.viewsets import HeroViewSet


router = routers.DefaultRouter()
router.register(r'heros', HeroViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
