# Generated by Django 4.2.7 on 2023-12-20 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_alter_attachment_name_alter_course_days_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='file',
            field=models.FileField(upload_to='%Y/%m/%d/'),
        ),
    ]