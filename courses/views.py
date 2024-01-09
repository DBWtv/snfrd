from django.shortcuts import render
from .models import Course
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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


def index(request):
    objects_list = Course.objects.all()

    items_per_page = 10
    paginator = Paginator(objects_list, items_per_page)

    page = request.GET.get('page')

    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)

    page_range = get_page_range(objects.number, paginator.num_pages)

    context = {
        'objects': objects,
        'page_range': page_range,
    }
    return render(request, 'index.html', context=context)


def get_page_range(current_page, total_pages):
    max_pages_before_and_after = 5
    if total_pages <= max_pages_before_and_after * 2 + 1:
        return range(1, total_pages + 1)
    elif current_page <= max_pages_before_and_after:
        return range(1, max_pages_before_and_after * 2 + 2)
    elif current_page >= total_pages - max_pages_before_and_after:
        return range(total_pages - max_pages_before_and_after * 2, total_pages + 1)
    else:
        return range(current_page - max_pages_before_and_after, current_page + max_pages_before_and_after + 1)
