from django.db import models
from django.contrib.auth.models import User
from main.models import Participant

class Score(models.Model):
    jury = models.ForeignKey(User, on_delete=models.CASCADE)  # Жюри
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)  # Участник
    technique = models.IntegerField()
    composition = models.IntegerField()
    creativity = models.IntegerField()
    impression = models.IntegerField()

    def get_average_score(self):
        return (self.technique + self.composition + self.creativity + self.impression) / 4
    
    def __str__(self):
        return f"Оценки от {self.jury} для {self.participant}"
