# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 15:01
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

def add_group_permissions(apps, schema_editor):
    group, created = Group.objects.get_or_create(name='default_user')
    if created:
        pass
        # add_thing = Permission.objects.get(codename='read_thing')
        # group.permissions.add()

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_slug'),
    ]

    operations = [
        migrations.RunPython(add_group_permissions)
    ]
