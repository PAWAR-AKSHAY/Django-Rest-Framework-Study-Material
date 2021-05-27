from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('student/', views.StudentList.as_view()),
    # path('student/', views.StudentCreate.as_view()),
    # path('student/<int:pk>', views.StudentRetrieve.as_view()),
    # path('student/<int:pk>', views.StudentUpdate.as_view()),
    # path('student/<int:pk>', views.StudentDestroy.as_view()),
    # path('student/<int:pk>', views.StudentRetrieveUpdate.as_view()),
    # path('student/<int:pk>', views.StudentRetrieveDestroy.as_view()),

    path('student/', views.StudentListCreate.as_view()),
    path('student/<int:pk>', views.StudentRetrieveUpdateDestroy.as_view()),
]

