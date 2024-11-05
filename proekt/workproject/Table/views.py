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


def get_scores(request, participant_id):
    if request.method == 'GET':
        scores = Score.objects.filter(participant_id=participant_id).select_related('jury')
        scores_data = []
        for score in scores:
            scores_data.append({
                'jury': score.jury.username,
                'technique': score.technique,
                'composition': score.composition,
                'creativity': score.creativity,
                'impression': score.impression,
                'average_score': score.get_average_score(),
            })
        return JsonResponse(scores_data, safe=False)

