# Generated by Django 3.2.6 on 2021-08-11 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='email_name',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='details',
            old_name='first_name',
            new_name='employee_deparment',
        ),
        migrations.RenameField(
            model_name='details',
            old_name='last_name',
            new_name='employee_name',
        ),
        migrations.RemoveField(
            model_name='details',
            name='phone_name',
        ),
    ]
