# Generated by Django 4.2.7 on 2023-12-05 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_lecture_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lecture',
            options={},
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='number',
        ),
        migrations.AddField(
            model_name='lecture',
            name='day',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='lectures', to='courses.day'),
            preserve_default=False,
        ),
    ]
