from django.core.management.base import BaseCommand
from courses.models import Day, DayNames


class Command(BaseCommand):
    help = 'Create week days'

    def handle(self, *args, **kwargs):
        for i, day in enumerate(DayNames.choices):
            Day.objects.get_or_create(name=day[0], order=i)

        self.stdout.write(self.style.SUCCESS('Days created successfully'))
