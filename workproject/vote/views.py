from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ScoreForm
from .models import Score
from main.models import Participant  # Импортируем модель из другого приложения


@login_required
def vote_page(request):
    success_message = None

    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            score = form.save(commit=False)
            score.jury = request.user  # Текущий пользователь - жюри
            score.save()
            success_message = "Оценки успешно сохранены!"
            form = ScoreForm()  # Очищаем форму после успешного сохранения
    else:
        form = ScoreForm()

    participants = Participant.objects.all()  # Получаем всех участников для выбора

    return render(request, 'vote/vote.html',
                  {'form': form, 'participants': participants, 'success_message': success_message})