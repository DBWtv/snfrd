# Generated by Django 4.2.7 on 2023-12-05 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_remove_lecture_day'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lecture',
            options={'ordering': ['number']},
        ),
    ]