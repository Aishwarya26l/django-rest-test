# Generated by Django 3.2.9 on 2022-02-23 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20220223_1602'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='jobType',
            new_name='job_type',
        ),
    ]