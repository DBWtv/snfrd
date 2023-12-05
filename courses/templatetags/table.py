from django import template
from ..models import Lecture

register = template.Library()


@register.simple_tag(takes_context=True)
def get_head_days(context):
    course = context['course']
    return course.days.all()


@register.simple_tag(takes_context=True)
def get_weeks(context):
    course = context['course']
    return course.weeks.all()


@register.simple_tag(takes_context=True)
def get_lecture(context, week, day='Tuesday'):
    course = context['course']
    try:
        lecture = Lecture.objects.get(weeks=week, day=day)
    except Lecture.DoesNotExist:
        return None
    return lecture
