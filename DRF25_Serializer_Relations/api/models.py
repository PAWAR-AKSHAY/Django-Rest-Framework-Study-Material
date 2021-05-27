from django.db import models


class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='song')

    def __str__(self):
        return self.title
