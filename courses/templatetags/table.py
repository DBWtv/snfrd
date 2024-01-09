from django import template
from courses.models import Lecture
from courses.api.services import en_to_ru

register = template.Library()


@register.simple_tag(takes_context=True)
def get_head_days(context):
    course = context['course']
    return course.days.all()


@register.simple_tag(takes_context=True)
def get_weeks(context):
    course = context['course']
    return course.weeks.all()


@register.simple_tag
def get_lecture(week, day):
    try:
        lecture = Lecture.objects.get(weeks=week, day=day)
    except Lecture.DoesNotExist:
        return None
    return lecture



@register.filter(is_safe=True)
def translate_day(day):
    return en_to_ru(day)
