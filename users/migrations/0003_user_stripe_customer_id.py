# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-26 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stripe_customer_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]