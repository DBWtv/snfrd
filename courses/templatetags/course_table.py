from django import template
from django.utils.safestring import mark_safe
from ..models import Course, Week, Day, Lecture

register = template.Library()


@register.simple_tag(takes_context=True)
def get_course_title(context):
    course = context['course']
    is_admin = context['is_admin']
    title = get_title(course, is_admin)
    html = f'''
        <div class="row">
            {title}
        </div>
    '''
    return mark_safe(html)


@register.simple_tag(takes_context=True)
def get_course_about(context):
    course = context['course']
    is_admin = context['is_admin']
    about = get_about(course, is_admin)
    info = get_info(course, is_admin)
    html = f'''
        <div class="row">
            {about}
            {info}
        </div>
    '''
    return mark_safe(html)


@register.simple_tag(takes_context=True)
def get_table_body(context):
    course = context['course']
    is_admin = context['is_admin']
    weeks, days, lectures = get_table(course)
    return mark_safe(''.join(table_rows(weeks, days, lectures, is_admin)))


@register.simple_tag(takes_context=True)
def get_table_head(context):
    course = context['course']
    days = get_table(course)[1]
    html = '''
        <th>Week</th>
        {days}
    '''

    days_html = ''.join(f'<th>{day.name}</th>' for day in days)

    return mark_safe(html.format(days=days_html))


def table_rows(weeks: list[Week], days: list[Day], lectures: list[Lecture], is_admin: bool = False):
    svg = '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 20 20"><path fill="#888888" d="M10 1.6a8.4 8.4 0 1 0 0 16.8a8.4 8.4 0 0 0 0-16.8zm5 9.4h-4v4H9v-4H5V9h4V5h2v4h4v2z"/></svg>'
    button = f'<button class="btn btn-sm" id="addLecture" style="margin-left:1em;">{svg}</button>'

    rows = []

    html = '''
        <tr>
            <td>{week_number}</td>
            {lectures}
        </tr>
    '''

    for week in weeks:
        lectures_html = ''
        for day in days:
            lecture = get_lectures(day, week, lectures)
            if lecture != '<div class="lectures"></div>':
                lectures_html += f'<td>{lecture}</td>'
            if lecture == '<div class="lectures"></div>':
                lectures_html += f'<td>{button if is_admin else ""}</td>'
        rows.append(html.format(
            week_number=week.week_number, lectures=lectures_html))
    return rows


def get_lectures(day: Day, week: Week, lectures: list[Lecture]):
    html = '<div class="lectures">{lectures}</div>'
    lectures_html = ''
    for lecture in lectures:
        if lecture.day == day and lecture.weeks.all().first() == week:
            lectures_html += f'<div class="date">{lecture.date}</div>'
            lectures_html += f'<div class="lecture">{lecture.title}</div>'
            lectures_html += '''<div class="classLinks">
                                    <!-- slides -->
                                    <!-- If there are slides, show them -->
                                    <a href="lectures/CS106L Welcome - F23.pdf">
                                         📖 Slides
                                    </a>
                                    <br>
                                        <a href="policies.html">
                                             📃 Policies
                                        </a>
                                    <br>
                                </div>'''

    return mark_safe(html.format(lectures=lectures_html))


def get_about(course: Course, is_admin: bool = True):
    course_lines = course.description.split('\n')
    course_lines = [line for line in course_lines if line != '\r']
    lines = ''.join(
        f'<p class="description">{line}</p>' if not is_admin else line for line in course_lines
    )
    html = f'''
    <div class="col-lg-8">
        <div class="content-bottom">
            <h2 style="font-size:1.25em; font-weight:700;">About {course.id.upper()}</h2>
            {f'<textarea class="form-control" id="courseInfo" rows="{len(course_lines)}">'if is_admin else ''}{lines}{'</textarea>' if is_admin else ''}
        </div>
    </div>
    '''
    return mark_safe(html)


def get_info(course: Course, is_admin: bool = True):
    info_lines = course.info.split('\n')
    info_lines = [line for line in info_lines if line != '\r']
    lines = ''.join(
        '<p class="description" style="margin-bottom:.45em">{line}</p>'.format(line=line.strip('\r')) if not is_admin else line for line in info_lines
    )
    html = f'''
    <div class="col-lg-4">
        <div class="content-bottom bg-alt">
            <h3 style="font-size:1.25em; font-weight:700;">Course Information</h3>
            {f'<textarea class="form-control" id="courseInfo" rows="{len(info_lines)}">'if is_admin else ''}{lines}{'</textarea>' if is_admin else ''}
        </div>
    </div>
    '''
    return mark_safe(html)


def get_title(course: Course, is_admin: bool = True):

    lines = course.title.split('\n')
    lines = [line for line in lines if line != '\r']
    lines_html = ''
    for index in range(len(lines)):
        if index == 0:
            if is_admin:
                lines_html += f'{lines[index]}'
            else:
                lines_html += f'<h1 style="font-size:3.25em; font-weight:700; margin:0 0;">{lines[index]}</h1>'
        else:
            if is_admin:
                lines_html += f'{lines[index]}'
            else:
                lines_html += f'<h3>{lines[index]}</h3>'

    html = f'''
    <div class="col-lg-12">
        <div class="content-top">
            {'<textarea class="form-control" id="courseInfo">'if is_admin else ''}{lines_html}{'</textarea>' if is_admin else ''}
        </div>
    </div>
    '''
    return mark_safe(html)


def get_table(course: Course) -> tuple[list[Week], list[Day], list[Lecture]]:
    days: list[Day] = [day for day in course.days.all()]
    weeks: list[Week] = [week for week in course.weeks.all()]
    lectures: list[Lecture] = []
    for week in weeks:
        for lecture in week.lectur.all():
            lectures.append(lecture)

    return weeks, days, lectures
