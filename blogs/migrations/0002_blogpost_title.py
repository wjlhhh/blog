# Generated by Django 2.0.6 on 2018-06-11 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
