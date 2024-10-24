from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ScoreForm
from .models import Score
from main.models import Participant  # Импортируем модель из другого приложения
from django.http import JsonResponse
from django.http import HttpResponseForbidden

@login_required
def vote_page(request):
    success_message = None
    error_message = None

    # Получаем все оценки текущего пользователя
    scores = Score.objects.filter(jury=request.user)

    if request.method == 'POST':
        form = ScoreForm(request.POST)

        if form.is_valid():
            participant = form.cleaned_data['participant']
            # Проверяем, существует ли уже оценка для данного участника от текущего пользователя
            existing_score = Score.objects.filter(jury=request.user, participant=participant).first()

            if existing_score:
                error_message = "Вы уже оценили данного участника!"
            else:
                score = form.save(commit=False)
                score.jury = request.user  # Текущий пользователь - жюри
                score.save()
                success_message = "Оценки успешно сохранены!"
                form = ScoreForm()  # Очищаем форму после успешного сохранения
    else:
        form = ScoreForm()

    participants = Participant.objects.all()  # Получаем всех участников для выбора

    return render(request, 'vote/vote.html', {
        'form': form,
        'participants': participants,
        'success_message': success_message,
        'error_message': error_message,
        'scores': scores,  # Передаем все оценки текущего пользователя
    })


@login_required
def edit_score(request, score_id):
    score = get_object_or_404(Score, id=score_id)

    if request.method == 'POST':
        form = ScoreForm(request.POST, instance=score)
        if form.is_valid():
            form.save()
            return redirect('vote_page')  # Перенаправляем на страницу голосования с сообщением об успехе
    else:
        form = ScoreForm(instance=score)

    return render(request, 'vote/edit_score.html', {
        'form': form,
        'score': score,
    })


def delete_score(request, score_id):
    score = get_object_or_404(Score, id=score_id)

    # Проверка, что текущий пользователь является автором оценки
    if score.jury != request.user:
        return HttpResponseForbidden("У вас нет прав на удаление этой оценки.")

    score.delete()
    return redirect('vote_page')