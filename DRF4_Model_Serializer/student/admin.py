from django.contrib import admin
from student import models


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'city')
