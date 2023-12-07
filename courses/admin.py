from django.contrib import admin
from .models import Course, Lecture, Week, Day, Attachment

admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(Week)
admin.site.register(Day)
admin.site.register(Attachment)
