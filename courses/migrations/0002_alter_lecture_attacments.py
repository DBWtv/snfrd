# Generated by Django 4.2.7 on 2023-12-05 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='attacments',
            field=models.ManyToManyField(blank=True, related_name='lecture', to='courses.attachment'),
        ),
    ]
