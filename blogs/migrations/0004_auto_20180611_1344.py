# Generated by Django 2.0.6 on 2018-06-11 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20180611_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='dade_added',
            new_name='date_added',
        ),
    ]
