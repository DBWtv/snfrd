from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from .services import (
    get_course_weeks,
    create_weeks,
    get_course_days,
    add_work_day,
)
from django.shortcuts import render


@require_POST
def add_row_api(request):
    try:
        # get post data
        course_id = request.POST.get('course_id')
        week_id = request.POST.get('week_id')

        # get course and weeks in course
        course, course_weeks = get_course_weeks(course_id)

        # create new week and add to course
        create_weeks(course, course_weeks, week_id)

        return HttpResponse(status=201)
    except Exception as e:
        print(e)
        return HttpResponse(status=400)


@require_POST
def enable_days(request):
    return JsonResponse(get_course_days(request.POST['course_id']), safe=False)


@require_POST
def update_table(request):
    course = get_course_weeks(request.POST['course_id'])[0]
    contex = {
        'course': course,
    }
    add_work_day(course, request.POST['day_id'])
    return HttpResponse('ok', status=201)
