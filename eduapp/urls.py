from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('wip', work_in_progress, name='wip')
]