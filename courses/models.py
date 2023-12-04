from django.db import models


class DayNames(models.TextChoices):
    mond = 'Monday'
    tusd = 'Tuesday'
    wdns = 'Wednesday'
    thsd = 'Thursday'
    frdy = 'Friday'
    satd = 'Saturday'
    sudy = 'Sunday'


class Day(models.Model):
    name = models.CharField(max_length=10, choices=DayNames.choices)

    def __str__(self) -> str:
        return self.name


class Lecture(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=255)
    day = models.ForeignKey(
        Day, on_delete=models.CASCADE, related_name='lectures'
    )

    def __str__(self):
        return self.title


class Week(models.Model):
    lectur = models.ManyToManyField(Lecture, related_name='weeks')
    week_number = models.IntegerField()

    def __str__(self):
        return f'week - {self.week_number} - {self.course.all().first()}'


class Course(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    title = models.TextField(max_length=255)
    description = models.TextField()
    info = models.TextField()
    days = models.ManyToManyField(Day, related_name='course')
    weeks = models.ManyToManyField(Week, related_name='course')

    def __str__(self):
        return self.title
