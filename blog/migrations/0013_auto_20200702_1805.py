# Generated by Django 3.0.5 on 2020-07-02 12:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200701_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 2, 12, 35, 11, 8566, tzinfo=utc)),
        ),
    ]
