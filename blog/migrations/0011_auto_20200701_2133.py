# Generated by Django 3.0.5 on 2020-07-01 16:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200701_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 16, 3, 57, 308069, tzinfo=utc)),
        ),
    ]
