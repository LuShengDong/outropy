# Generated by Django 2.0.2 on 2018-02-07 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_auto_20180207_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='importance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='scheduled_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
