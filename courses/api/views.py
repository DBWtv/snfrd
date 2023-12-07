from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .services import get_course_weeks, create_weeks


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
