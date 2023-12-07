from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def get_course_title(context):
    course = context['course']
    return [line.strip('\r') for line in course.title.split('\n')]


@register.simple_tag(takes_context=True)
def get_course_info(context):
    course = context['course']
    return [line.strip('\r') for line in course.info.split('\n')]


@register.simple_tag(takes_context=True)
def get_course_about(context):
    course = context['course']
    return [line.strip('\r') for line in course.description.split('\n')]
