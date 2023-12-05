from django.shortcuts import render
from .models import Course
from django.http import Http404


def index(request, id: str):
    try:
        course = Course.objects.get(id=id)
    except Course.DoesNotExist:
        raise Http404('Course does not exist')

    if request.user.is_superuser:
        return render(request, 'courses/admin/course.html', {'course': course})

    return render(request, 'courses/course.html', {'course': course})
