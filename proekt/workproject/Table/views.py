from django.shortcuts import render, get_object_or_404
from main.models import Participant
from vote.models import Score
from .forms import ParticipantSearchForm
from django.http import JsonResponse


def get_all_scores(request):
    participants = Participant.objects.all()
    all_scores_data = []

    for participant in participants:
        scores = Score.objects.filter(participant=participant)

        # Если у участника нет оценок, можно вручную добавить пустые значения
        if not scores:
            participant_scores = [{
                'jury': 'Нет данных',
                'participant_number': participant.number,
                'participant_name': participant.name,
                'technique': 0,
                'composition': 0,
                'creativity': 0,
                'impression': 0,
                'score_sum': 0  # Сумма баллов для участника без оценок
            }]
        else:
            participant_scores = [
                {
                    'jury': score.jury.username,
                    'participant_number': participant.number,
                    'participant_name': participant.name,
                    'technique': score.technique,
                    'composition': score.composition,
                    'creativity': score.creativity,
                    'impression': score.impression,
                    'score_sum': score.technique + score.composition + score.creativity + score.impression
                }
                for score in scores
            ]

        all_scores_data.extend(participant_scores)

    return JsonResponse(all_scores_data, safe=False)


def all_participants_scores(request):
    participants = Participant.objects.all()
    all_scores = {}

    for participant in participants:
        scores = Score.objects.filter(participant=participant)
        scores_data = []
        total_score = 0  # Переменная для хранения суммы баллов участника
        for score in scores:
            # Суммируем баллы по всем критериям
            score_sum = score.technique + score.composition + score.creativity + score.impression
            total_score += score_sum  # Добавляем к общей сумме

            # Собираем данные по каждому участнику
            scores_data.append({
                'jury': score.jury.username,
                'technique': score.technique,
                'composition': score.composition,
                'creativity': score.creativity,
                'impression': score.impression,
                'score_sum': score_sum,  # Добавляем сумму баллов для каждого участника
            })

        all_scores[participant] = {
            'scores': scores_data,
            'total_score': total_score,  # Общая сумма баллов для участника
            'votes_count': len(scores),  # Количество оценок для участника
        }

    # Сортировка участников по количеству оценок
    sorted_participants = sorted(all_scores.items(), key=lambda x: x[1]['votes_count'], reverse=True)

    # Добавление рейтинга
    ranked_participants = []
    rank = 1
    for participant, data in sorted_participants:
        ranked_participants.append({
            'rank': rank,
            'participant_number': participant.number,
            'participant_name': participant.name,
            'total_score': data['total_score'],
        })
        rank += 1

    return render(request, 'Table/table.html', {
        'sorted_participants': sorted_participants,
        'ranked_participants': ranked_participants,  # Передаем отсортированных участников
    })