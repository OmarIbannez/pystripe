# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-23 21:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('amount', models.IntegerField()),
                ('currency', models.CharField(max_length=10)),
                ('plan_id', models.CharField(max_length=255)),
                ('interval', models.CharField(blank=True, max_length=10, null=True)),
                ('interval_count', models.IntegerField()),
                ('livemode', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('trial_period_days', models.IntegerField()),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
