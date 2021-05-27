from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from api import views

# Creating Router Object
router = DefaultRouter()

# Register ViewSet with router
router.register('singer', views.SingerViewSet, basename='singer')
router.register('song', views.SongViewSet, basename='song')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
