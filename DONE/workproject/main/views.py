from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Participant
from .forms import ParticipantForm

# Create your views here.
@login_required
def main(request):
    return render(request, 'main/main.html')

def participant_list(request):
    participants = Participant.objects.all()
    return render(request, 'main/participant_list.html', {'participants': participants})

# Добавление участника
def participant_create(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm()
    return render(request, 'main/participant_form.html', {'form': form})

# Редактирование участника
def participant_edit(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm(instance=participant)
    return render(request, 'main/participant_form.html', {'form': form})

# Удаление участника
def participant_delete(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    if request.method == 'POST':
        participant.delete()
        return redirect('participant_list')
    return render(request, 'main/participant_confirm_delete.html', {'participant': participant})

def delete_all_participants(request):
    if request.method == 'POST':
        Participant.objects.all().delete()  # Удаляем всех участников
        return redirect('participant_list')  # Перенаправляем на страницу списка участников