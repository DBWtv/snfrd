from django.shortcuts import render
from .models import Course
from django.http import Http404


def get_course(id: str):
    try:
        return Course.objects.get(id=id)
    except Course.DoesNotExist:
        raise Http404('Course does not exist')


def course(request, id: str):
    course = get_course(id)

    return render(request, 'courses/course.html', {'course': course})


def course_admin(request, id: str):
    course = get_course(id)

    if not request.user.is_superuser:
        raise Http404('Page not found')

    return render(request, 'courses/admin/course.html', {'course': course})
