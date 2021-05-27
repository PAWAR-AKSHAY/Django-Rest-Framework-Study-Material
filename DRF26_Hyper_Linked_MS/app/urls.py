from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from student import views

router = DefaultRouter()
router.register('student', views.StudentViewSet, basename='student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
