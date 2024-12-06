# Generated by Django 5.1.1 on 2024-10-21 18:44

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning_cases', '0005_planning_case_parcel_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='area_of_interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('notes', models.TextField(blank=True)),
                ('geometry', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]