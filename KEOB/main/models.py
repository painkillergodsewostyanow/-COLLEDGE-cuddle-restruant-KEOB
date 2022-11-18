from django.db import models


class Food(models.Model):
    photo = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    weight = models.IntegerField(blank=True)
    cost = models.IntegerField(blank=True)

