from django.http import HttpResponse
from django.shortcuts import render
from .models import GridSubject, Teacher


def index(request):
    return render(request, 'eduapp/index.html',
                  {'title': 'main',
                   'grid_subjects': GridSubject.objects.all(),
                   'teachers': Teacher.objects.all()})


def handle_not_found(request):
    return render((request, 'eduapp/not-found.html'))