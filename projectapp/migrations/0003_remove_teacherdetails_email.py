# Generated by Django 4.2.7 on 2023-11-28 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0002_teacherdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherdetails',
            name='email',
        ),
    ]
