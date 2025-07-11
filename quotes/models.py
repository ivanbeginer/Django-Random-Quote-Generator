from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

class Source(models.Model):
    TYPE_CHOICES = [('Movie','Фильм'),('Book','Книга'),('Series','Сериал')]
    name = models.CharField(max_length=255,null=False, verbose_name='Название')
    author = models.CharField(max_length=255, blank=True,verbose_name='Автор')
    year = models.PositiveIntegerField(null=True,verbose_name='Год')
    type = models.CharField(max_length=255,choices=TYPE_CHOICES,verbose_name='Тип')
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Источник'
        verbose_name_plural = 'Источники'

class Quote(models.Model):
    text = models.CharField(max_length=255,null=False,verbose_name='Текст')
    source = models.ForeignKey(Source,on_delete=models.CASCADE,verbose_name='Источник')
    weight = models.PositiveIntegerField(default=1,verbose_name='Вес')
    views = models.PositiveIntegerField(default=0,verbose_name='Просмотры')
    likes = models.PositiveIntegerField(default=0,verbose_name='Лайки')
    dislikes = models.PositiveIntegerField(default=0,verbose_name='Дизлайки')

    def less_than_three(self):
        if self.pk is None and Quote.objects.filter(source = self.source).count()>3:
            raise ValidationError('У одного ситочника не может быть больше трех цитат')
    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'