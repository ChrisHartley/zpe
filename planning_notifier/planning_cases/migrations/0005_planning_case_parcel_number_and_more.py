# Generated by Django 5.1.1 on 2024-10-16 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning_cases', '0004_alter_planning_case_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='planning_case',
            name='parcel_number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='planning_case',
            name='case_number',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
