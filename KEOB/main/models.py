from django.db import models


class Food(models.Model):
    photo = models.ImageField(upload_to='photos/', verbose_name='фото')
    title = models.CharField(max_length=255, verbose_name='заголовок')
    weight = models.CharField(max_length=255, verbose_name='вес')
    cost = models.IntegerField(blank=True, verbose_name='цена')

    def __str__(self):
        return f"{self.photo, self.title, self.weight, self.cost}"

    class Meta:
        verbose_name = 'Блюда'
        verbose_name_plural = 'Блюда'
        ordering = ['pk']

