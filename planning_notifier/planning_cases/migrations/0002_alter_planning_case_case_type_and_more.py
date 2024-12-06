# Generated by Django 5.1.1 on 2024-10-01 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning_cases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planning_case',
            name='case_type',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='planning_case',
            name='description',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='planning_case',
            name='location',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='planning_case',
            name='owner',
            field=models.CharField(blank=True, max_length=1024),
        ),
    ]
