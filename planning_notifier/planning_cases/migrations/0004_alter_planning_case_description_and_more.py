# Generated by Django 5.1.1 on 2024-10-11 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning_cases', '0003_planning_case_case_date_planning_case_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planning_case',
            name='description',
            field=models.TextField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='planning_case',
            name='location',
            field=models.TextField(blank=True, max_length=1024),
        ),
    ]
