from django.shortcuts import render
from .forms import BirthdayForm
from .utils import calculate_birthday_countdown
from .models import Birthday  # <--- Должно быть в импортах

def birthday(request):
    form = BirthdayForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        form.save()
        birthday_date = form.cleaned_data['birthday']
        countdown = calculate_birthday_countdown(birthday_date)
        context['birthday_countdown'] = countdown

    return render(request, 'birthday/birthday.html', context)

def birthday_list(request):
    birthdays = Birthday.objects.all()
    context = {'birthdays': birthdays}
    return render(request, 'birthday/birthday_list.html', context)