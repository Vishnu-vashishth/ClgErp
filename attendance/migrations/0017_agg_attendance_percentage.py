# Generated by Django 4.1.7 on 2023-04-05 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0016_total_attendance_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='agg_attendance',
            name='percentage',
            field=models.FloatField(default=0),
        ),
    ]
