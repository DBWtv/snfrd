# Generated by Django 4.2.7 on 2023-11-30 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='weeks',
            field=models.ManyToManyField(related_name='course', to='courses.week'),
        ),
    ]
