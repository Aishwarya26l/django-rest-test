# Generated by Django 3.2.9 on 2022-02-23 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20220223_1618'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ('updated_at',)},
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]