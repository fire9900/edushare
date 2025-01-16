from django.shortcuts import render
from .models import Course, LessonList


def courses(request):
    tags = request.GET.getlist('tags')
    filtered_courses = Course.objects.filter(tags__title__in=tags) if tags else Course.objects.all()
    return render(request, 'courses/courses.html', {'title': 'Курсы', 'courses': filtered_courses})


def course_landing(request, id):
    current_course = Course.objects.filter(id=id).first()
    return render(request, 'courses/course_landing.html',
                  {'title': current_course.title,
                   'course': current_course,
                   'lesson_list': LessonList.objects.filter(related_course__pk=id)})


def lesson_page(request, id, slug):
    current_lesson = LessonList.objects.filter(related_course__pk=id).filter(slug=slug).first()
    return render(request, 'courses/lesson_page.html', {
        'lesson': current_lesson})
