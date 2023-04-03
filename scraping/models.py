from django.db import models

# Create your models here.


class Article(models.Model):
    url = models.CharField(max_length=255)
    headline = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date = models.DateTimeField()

    def __str__(self):
        return self.headline
