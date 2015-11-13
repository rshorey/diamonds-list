# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('service_type', models.CharField(choices=[('AUTO', 'Auto Repair'), ('LANDSCAPING', 'Landscaping'), ('TECH', 'Technology'), ('CREATIVE', 'Creative and Design'), ('COACHING', 'Coaching/Tutoring')], null=True, max_length=50, blank=True)),
                ('title', models.CharField(null=True, max_length=50, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('hourly_rate', models.IntegerField(null=True, blank=True)),
                ('has_references', models.NullBooleanField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('profile', models.TextField()),
                ('certifications', models.TextField(null=True, blank=True)),
                ('num_jobs_completed', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
