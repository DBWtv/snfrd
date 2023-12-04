from django.shortcuts import render
from .models import Course
from django.http import Http404


def index(request, id: str):
    try:
        course = Course.objects.get(id=id)
    except Course.DoesNotExist:
        raise Http404('Course does not exist')
    return render(request, 'courses/course.html', {'course': course, 'is_admin': request.user.is_superuser})
