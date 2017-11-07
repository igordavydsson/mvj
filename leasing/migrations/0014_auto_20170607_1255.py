# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 09:55
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0013_remove_areas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='mpoly',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
        ),
    ]