# Generated by Django 2.2.5 on 2019-09-21 07:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('foodtruck', '0006_auto_20190921_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodtruckcomment',
            name='ftCommentTimeStamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 21, 7, 8, 54, 453384, tzinfo=utc)),
        ),
    ]
