# Generated by Django 5.1.4 on 2024-12-19 01:05

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planning_cases', '0009_alter_area_of_interest_planning_cases'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area_of_interest',
            name='planning_cases',
        ),
        migrations.AddField(
            model_name='planning_case',
            name='geometry_poly',
            field=django.contrib.gis.db.models.fields.PolygonField(blank=True, default=1, srid=4326),
            preserve_default=False,
        ),
    ]