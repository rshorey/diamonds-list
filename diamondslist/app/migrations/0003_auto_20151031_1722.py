# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_listing_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='certifications',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='has_references',
            field=models.NullBooleanField(),
        ),
    ]
