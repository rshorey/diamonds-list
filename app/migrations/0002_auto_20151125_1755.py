# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(null=True, max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='reason_for_joining',
            field=models.TextField(null=True, help_text="Why did this person make an account on Diamond's List?", blank=True),
        ),
    ]
