from django.contrib import admin
from api import models


@admin.register(models.Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender']


@admin.register(models.Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'duration', 'singer']
