from django.db import models


class Food(models.Model):
    photo = models.ImageField(upload_to='photos/', verbose_name='фото')
    title = models.CharField(max_length=255, verbose_name='заголовок')
    weight = models.CharField(max_length=255, verbose_name='вес')
    cost = models.IntegerField(blank=True, verbose_name='цена')

    def __str__(self):
        return f"{self.photo, self.title, self.weight, self.cost}"

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        ordering = ['pk']


class Post(models.Model):
    name = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    txt = models.TextField(blank=False)

    def __str__(self):
        return f"{self.name, self.txt, self.time_create}"

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коментарии'
        ordering = ['time_create']
