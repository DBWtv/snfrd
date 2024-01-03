from collections.abc import Iterable
from typing import Any
from django.db import models


class Attachment(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to='%Y/%m/%d/')

    def __str__(self):
        if self.name is None:
            return self.file.name
        return self.name

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)


class DayNames(models.TextChoices):
    mond = 'Monday'
    tusd = 'Tuesday'
    wdns = 'Wednesday'
    thsd = 'Thursday'
    frdy = 'Friday'
    satd = 'Saturday'
    sudy = 'Sunday'


class Day(models.Model):
    name = models.CharField(
        max_length=10,
        choices=DayNames.choices,
        unique=True
    )
    order = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['order']


class Lecture(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=255)
    day = models.ForeignKey(
        Day, on_delete=models.CASCADE, related_name='lectures',
        blank=True, null=True,
    )
    attacments = models.ManyToManyField(
        Attachment,
        related_name='lecture',
        blank=True
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.day:
            self.day = Day.objects.get(name=self.date.strftime('%A'))
        super().save(*args, **kwargs)

    @property
    def str_date(self):
        return self.date.strftime('%d. %m. %Y')


class Week(models.Model):
    lectur = models.ManyToManyField(Lecture, related_name='weeks')
    week_number = models.IntegerField()

    def __str__(self):
        return f'week - {self.week_number} - {self.course.all().first()}'


class Course(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    title = models.TextField(max_length=255, unique=True)
    description = models.TextField()
    info = models.TextField()
    days = models.ManyToManyField(Day, related_name='course', blank=True)
    weeks = models.ManyToManyField(Week, related_name='course', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.title.lower().replace(' ', '-')
        super().save(*args, **kwargs)

    @property
    def url(self):
        return f'/class/{self.id}/'
    
    class Meta:
        ordering = ['pk']
