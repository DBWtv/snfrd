from courses.models import Course, Week, Day, Attachment, Lecture
from django.http import HttpResponse
import json


class InvalidData(Exception):
    def __init__(self, message: list[dict]):
        self.message = message


def get_lecture(lecture_id: str, *args, **kwargs) -> Lecture | HttpResponse:
    '''
    Get lecture by week, day and course
    '''
    try:
        lecture = Lecture.objects.get(id=lecture_id)
    except Lecture.DoesNotExist:
        return HttpResponse(status=404)

    return lecture


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
    for week in course_weeks:
        if week.week_number == week_id:
            return HttpResponse(status=400)

    try:
        week = Week.objects.create(week_number=week_id)
        course_weeks.append(week)
        course.weeks.set(course_weeks)
    except Exception as e:
        print(e)
        return HttpResponse(status=400)


def get_course_days(course_id: int, not_found_status: int = 404) -> list | HttpResponse:
    '''
    Get free days for course
    '''
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return HttpResponse(status=not_found_status)

    try:
        course_days_ids = course.days.values_list('id', flat=True)
        enabled_days = Day.objects.exclude(
            id__in=course_days_ids).values('id', 'name')

        for day in enabled_days:
            day['name'] = en_to_ru(day['name'])

    except Day.DoesNotExist:
        return HttpResponse(status=400)

    return list(enabled_days)


def add_work_day(course: Course, day_id: int) -> None | HttpResponse:
    '''
    Add work day to course
    '''
    course_days = [day for day in course.days.all()]
    day = Day.objects.get(id=day_id)
    try:
        if day in course_days:
            return HttpResponse(status=400)
        course_days.append(day)
        course.days.set(course_days)
    except Exception as e:
        print(e)
        return HttpResponse(status=400)


def body_to_dict(func: callable):
    def wrapper(request):
        request.POST = json.loads(request.body)
        return func(request)
    return wrapper


def validate_about(data: dict) -> bool:
    '''
    Validate about form
    '''
    anable_fields = ['title', 'description', 'info']

    errors = []

    field = data.get('field', None)
    text = data.get('text', None)
    course_id = data.get('course_id', None)

    if field == '' or None:
        errors.append({'field': 'field is empty'})
    if text == '' or None:
        errors.append({'text': 'text is empty'})
    if course_id == '' or None:
        errors.append({'course_id': 'course_id is empty'})

    if field not in anable_fields:
        errors.append({'field': 'should be title, description or info'})

    if len(errors) > 0:
        raise InvalidData(errors)

    return True


def add_r_to_end(text):
    '''
    Add \r before \n of each line
    '''
    return text.replace('\n', '\r\n')


def add_file_to_lecture(lecture_id, file, name):
    '''
    Add file to lecture
    '''
    new_attachment = Attachment.objects.create(
        file=file, name=name)

    try:
        lecture = Lecture.objects.get(id=lecture_id)
    except Lecture.DoesNotExist:
        return HttpResponse(status=404)

    new_attachment.save()
    attachments_list = [attachment for attachment in lecture.attacments.all()]
    attachments_list.append(new_attachment)
    lecture.attacments.set(attachments_list)
    lecture.save()
    return HttpResponse(status=201)


def en_to_ru(day: str) -> str:
    translation_map = {
        'Monday': 'Понедельник',
        'Tuesday': 'Вторник',
        'Wednesday': 'Среда',
        'Thursday': 'Четверг',
        'Friday': 'Пятница',
        'Saturday': 'Суббота',
        'Sunday': 'Воскресенье',
    }

    return translation_map.get(day, day)


def ru_to_en(day: str) -> str:
    translation_map = {
        'Понедельник': 'Monday',
        'Вторник': 'Tuesday',
        'Среда': 'Wednesday',
        'Четверг': 'Thursday',
        'Пятница': 'Friday',
        'Суббота': 'Saturday',
        'Воскресенье': 'Sunday',
    }

    return translation_map.get(day, day)
