from django.shortcuts import render, get_object_or_404
from main.models import Participant
from vote.models import Score
from .forms import ParticipantSearchForm
from django.http import JsonResponse


def participant_scores(request):
    form = ParticipantSearchForm()
    participant = None
    scores = None
    error_message = None  # Переменная для хранения сообщения об ошибке

    if request.method == 'POST':
        form = ParticipantSearchForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            try:
                participant = Participant.objects.get(number=number)
                scores = Score.objects.filter(participant=participant)

                # Проверяем, является ли запрос AJAX
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return render(request, 'Table/scores_table.html', {
                        'participant': participant,
                        'scores': scores,
                    })

            except Participant.DoesNotExist:
                error_message = "Неверный номер участника"

                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'error': error_message})

    # Возвращаем полный шаблон для обычного запроса
    return render(request, 'Table/table.html', {
        'form': form,
        'participant': participant,
        'scores': scores,
        'error_message': error_message,
    })




def get_all_scores(request):
    participants = Participant.objects.all()
    all_scores_data = []

    for participant in participants:
        scores = Score.objects.filter(participant=participant)
        participant_scores = [
            {
                'participant_number': participant.number,
                'participant_name': participant.name,
                'jury': score.jury.username,
                'technique': score.technique,
                'composition': score.composition,
                'creativity': score.creativity,
                'impression': score.impression,

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
        scores_data = [
            {
                'jury': score.jury.username,
                'technique': score.technique,
                'composition': score.composition,
                'creativity': score.creativity,
                'impression': score.impression,

            }
            for score in scores
        ]
        all_scores[participant] = scores_data

    return render(request, 'Table/table.html', {
        'all_scores': all_scores,
    })
