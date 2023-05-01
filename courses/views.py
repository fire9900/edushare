from django.shortcuts import render
from .models import Course


def courses(request):
    return render(request, 'courses/courses.html', {'title': 'Курсы', 'courses': Course.objects.all()})


def course_landing(request, id):
    current_course = Course.objects.filter(id=id).first()
    return render(request, 'courses/course_landing.html', {'title': current_course.title,
                                                           'course': current_course})
