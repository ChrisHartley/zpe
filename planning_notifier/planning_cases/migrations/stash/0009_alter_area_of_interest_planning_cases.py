# Generated by Django 5.1.4 on 2024-12-13 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning_cases', '0008_remove_area_of_interest_notes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area_of_interest',
            name='planning_cases',
            field=models.ManyToManyField(blank=True, null=True, to='planning_cases.planning_case'),
        ),
    ]
