# Generated by Django 3.2.9 on 2022-02-25 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20220223_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
