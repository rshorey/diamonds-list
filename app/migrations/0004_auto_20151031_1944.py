# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20151031_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='certifications',
        ),
        migrations.AddField(
            model_name='listing',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 19, 44, 25, 7242, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 19, 44, 38, 229552, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='certifications',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 19, 44, 47, 766197, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 19, 44, 53, 986419, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
