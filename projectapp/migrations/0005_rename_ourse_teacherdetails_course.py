# Generated by Django 4.2.7 on 2023-11-29 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0004_remove_teacherdetails_department_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacherdetails',
            old_name='ourse',
            new_name='course',
        ),
    ]