from courses.models import Course, Week
from django.http import HttpResponse


def get_course_weeks(course_id: int) -> tuple | HttpResponse:
    '''
    Get course and weeks in course
    '''
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return HttpResponse(status=404)
    return course, [week for week in course.weeks.all()]


def create_weeks(course: Course, course_weeks: list[Course], week_id: int) -> None | HttpResponse:
    '''
    Create new week and add to course
    '''
    try:
        week = Week.objects.create(week_number=week_id)
        course_weeks.append(week)
        course.weeks.set(course_weeks)
    except Exception as e:
        print(e)
        return HttpResponse(status=400)
