# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 19:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0007_thread_last_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='initial_post',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='initial_post', to='threads.Post'),
        ),
    ]