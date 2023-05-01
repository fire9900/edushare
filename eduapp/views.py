from django.http import HttpResponse
from django.shortcuts import render
from .models import GridSubject, Teacher


def index(request):
    return render(request, 'eduapp/index.html',
                  {'title': 'Главная',
                   'grid_subjects': GridSubject.objects.filter(on_index=True),
                   'teachers': Teacher.objects.filter(on_index=True)})


def work_in_progress(request):
    return render(request, 'eduapp/wip.html', {'title':'Работа в процессе'})


def handle_not_found(request):
    return render((request, 'eduapp/not-found.html'))
