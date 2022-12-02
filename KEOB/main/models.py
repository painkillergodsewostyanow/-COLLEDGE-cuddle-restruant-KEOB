from django.db import models
from django.core.validators import RegexValidator


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


class Book(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="'+999999999'")
    name = models.CharField(max_length=255, verbose_name='имя')
    phoneNumber = models.CharField(validators=[phone_regex], max_length=17, verbose_name="Номер телефона")
    email = models.EmailField(max_length=100, verbose_name='почта')
    numberOfPeople = models.IntegerField(verbose_name='количество человек')
    data = models.DateField(error_messages="не корректная дата", verbose_name='Дата')
    time = models.TimeField(error_messages="не корректное время", verbose_name='Время')
    reason = models.CharField(max_length=255, verbose_name='Повод посещения')
    accept = models.BooleanField(default=False, verbose_name='подтвержденно')
    isPass = models.BooleanField(default=False, verbose_name='прошло')


    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Бронь'
        ordering = ['data']






