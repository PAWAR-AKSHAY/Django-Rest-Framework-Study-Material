from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from student.auth import CustomAuthToken
from rest_framework.routers import DefaultRouter

from student import views

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('student', views.StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('gettoken/', obtain_auth_token),  # Using cmd python manage.py def_create_token <username>
    path('gettoken/', CustomAuthToken.as_view()),  # Custom token and using httpie
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
