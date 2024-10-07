from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Название', max_length=50, default='0')
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья', default='Введите текст')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta: #в панели админа переименовать
        verbose_name= 'Новость'
        verbose_name_plural = 'Новости'