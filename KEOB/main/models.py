from django.db import models


class Food(models.Model):
    photo = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=255)
    weight = models.IntegerField(blank=True)
    cost = models.IntegerField(blank=True)

    def __str__(self):
        return f"{self.photo, self.title, self.weight, self.cost}"
