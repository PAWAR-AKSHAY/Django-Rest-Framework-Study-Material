from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', views.student_api),
    path('student/<int:pk>', views.student_api),
]
