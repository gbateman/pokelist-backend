from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
import pokelist.views as views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'pokemon', views.PokemonViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
