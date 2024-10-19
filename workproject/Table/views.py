# views.py
from django.shortcuts import render
from vote.models import Score
from main.models import Participant

def participants_with_scores(request):
    participants_scores = []

    # Получаем всех участников
    participants = Participant.objects.all()

    # Для каждого участника собираем его оценки
    for participant in participants:
        scores = Score.objects.filter(participant=participant)

        # Рассчитываем средние оценки (или отображаем по отдельности)
        if scores.exists():
            total_technique = sum(score.technique for score in scores)
            total_composition = sum(score.composition for score in scores)
            total_creativity = sum(score.creativity for score in scores)
            total_impression = sum(score.impression for score in scores)
            score_count = scores.count()

            avg_technique = total_technique / score_count
            avg_composition = total_composition / score_count
            avg_creativity = total_creativity / score_count
            avg_impression = total_impression / score_count
        else:
            avg_technique = avg_composition = avg_creativity = avg_impression = 0

        participants_scores.append({
            'participant': participant,
            'avg_technique': avg_technique,
            'avg_composition': avg_composition,
            'avg_creativity': avg_creativity,
            'avg_impression': avg_impression,
        })

    return render(request, 'Table/Table.html', {
        'participants_scores': participants_scores,
    })