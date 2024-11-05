from django.db import models

class Participant(models.Model):
    number = models.PositiveIntegerField('Номер',unique=True)  # Уникальный номер участника
    name = models.CharField('Название', max_length=200)  # Имя участника

    def __str__(self):
        return f"{self.number} - {self.name}"

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'