# Generated by Django 5.1.4 on 2025-01-11 19:08

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='area_of_interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geometry', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='planning_case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_number', models.CharField(max_length=30, unique=True)),
                ('case_date', models.DateField()),
                ('case_type', models.CharField(blank=True, max_length=200)),
                ('location', models.TextField(blank=True, max_length=1024)),
                ('description', models.TextField(blank=True, max_length=1024)),
                ('owner', models.CharField(blank=True, max_length=1024)),
                ('case_url', models.URLField(blank=True)),
                ('geometry_pnt', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('geometry_poly', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4326)),
                ('parcel_number', models.CharField(blank=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
