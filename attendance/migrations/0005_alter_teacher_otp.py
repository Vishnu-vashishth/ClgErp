# Generated by Django 4.1.7 on 2023-04-02 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_alter_student_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='otp',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]
