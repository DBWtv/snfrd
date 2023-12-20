from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from .services import (
    get_course_weeks,
    create_weeks,
    get_course_days,
    add_work_day,
    body_to_dict,
    validate_about,
    InvalidData,
    add_r_to_end,
    add_file_to_lecture,
)
from .new_lecture_services import lecture_form_validate, append_lecture
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


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


@csrf_exempt
@body_to_dict
@require_POST
def add_lecture(request):
    try:
        lecture_form_validate(request.POST)
        append_lecture(request.POST)
    except Exception as e:
        try:
            return HttpResponse(e.message, status=400)
        except AttributeError:
            return HttpResponse(status=400)
    return HttpResponse('ok', status=201)


@csrf_exempt
@body_to_dict
@require_POST
def change_title(request):
    try:
        if validate_about(request.POST):
            course = get_course_weeks(request.POST['course_id'])[0]
            setattr(
                course,
                request.POST['field'],
                add_r_to_end(request.POST['text'])
            )
            course.save()
    except InvalidData as e:
        return JsonResponse(e.message, status=400, safe=False)
    return HttpResponse(content=getattr(course, request.POST['field']), status=201)


@csrf_exempt
@require_POST
def add_file(request):
    try:
        add_file_to_lecture(
            lecture_id=request.POST['lecture_id'],
            file=request.FILES['file'],
            name=request.POST['name']
        )
    except Exception as e:
        print(e)
        return HttpResponse(status=400)
