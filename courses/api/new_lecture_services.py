from courses.models import Week, Day, Lecture
from datetime import datetime
from .services import ru_to_en


class InvalidData(Exception):
    def __init__(self, message: list[dict]):
        self.message = message


def append_lecture(data: dict) -> Lecture | None:
    week = get_week(data.get('course_id'), data.get('week_id'))
    lectures = [lecture for lecture in week.lectur.all()]
    lectures.append(make_lecture(data))
    week.lectur.set(lectures)
    week.save()


def make_lecture(data: dict) -> Lecture:
    lecture = Lecture(
        date=data.get('date'),
        title=data.get('title'),
        day=Day.objects.get(name=datetime.strptime(
            data.get('date'), '%Y-%m-%d').strftime("%A")),
    )
    lecture.save()
    return lecture


def get_week(course_id: int, week_id: int) -> Week | None:
    try:
        week = Week.objects.get(week_number=week_id, course__id=course_id)
    except Week.DoesNotExist:
        raise InvalidData([{'week': 'week does not exist'}])
    return week


def lecture_form_validate(data: dict) -> bool | InvalidData:
    errors = []
    day: datetime = datetime.strptime(
        data.get('date'), '%Y-%m-%d').strftime("%A")
    if day != data.get('day'):
        data['day'] = ru_to_en(day)
        if day != data.get('day'):
            errors.append({'day': 'day is not equal to date'})
    if data.get('title') == '':
        errors.append({'title': 'title is empty'})

    if errors:
        raise InvalidData(errors)
    return True
