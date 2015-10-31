# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('service_type', models.CharField(blank=True, null=True, choices=[('AUTO', 'Auto Repair'), ('LANDSCAPING', 'Landscaping')], max_length=50)),
                ('description', models.TextField(null=True, blank=True)),
                ('hourly_rate', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('firstname', models.CharField(blank=True, null=True, max_length=200)),
                ('lastname', models.CharField(blank=True, null=True, max_length=200)),
                ('profile', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='user',
            field=models.ForeignKey(to='app.User'),
        ),
    ]
