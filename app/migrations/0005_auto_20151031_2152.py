# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20151031_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='num_jobs_completed',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='listing',
            name='service_type',
            field=models.CharField(max_length=50, blank=True, null=True, choices=[('AUTO', 'Auto Repair'), ('LANDSCAPING', 'Landscaping'), ('TECH', 'Technology'), ('CREATIVE', 'Creative and Design'), ('COACHING', 'Coaching/Tutoring')]),
        ),
    ]
