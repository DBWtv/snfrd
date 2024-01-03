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
    # Получаем список объектов (ваш запрос)
    your_objects_list = Course.objects.all()

    # Устанавливаем количество объектов на странице
    items_per_page = 10
    paginator = Paginator(your_objects_list, items_per_page)

    # Получаем текущую страницу из параметра GET запроса
    page = request.GET.get('page')

    try:
        # Получаем объекты для текущей страницы
        your_objects = paginator.page(page)
    except PageNotAnInteger:
        # Если 'page' не является целым числом, берем первую страницу
        your_objects = paginator.page(1)
    except EmptyPage:
        # Если 'page' больше, чем общее количество страниц, берем последнюю страницу
        your_objects = paginator.page(paginator.num_pages)

    # Получаем диапазон страниц для отображения
    page_range = get_page_range(your_objects.number, paginator.num_pages)

    context = {
        'your_objects': your_objects,
        'page_range': page_range,
    }
    return render(request, 'index.html', context=context)


def get_page_range(current_page, total_pages):
    # Определяем диапазон страниц для отображения
    max_pages_before_and_after = 5
    if total_pages <= max_pages_before_and_after * 2 + 1:
        return range(1, total_pages + 1)
    elif current_page <= max_pages_before_and_after:
        return range(1, max_pages_before_and_after * 2 + 2)
    elif current_page >= total_pages - max_pages_before_and_after:
        return range(total_pages - max_pages_before_and_after * 2, total_pages + 1)
    else:
        return range(current_page - max_pages_before_and_after, current_page + max_pages_before_and_after + 1)
