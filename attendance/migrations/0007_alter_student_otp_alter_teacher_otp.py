# Generated by Django 4.1.7 on 2023-04-02 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0006_alter_student_otp_alter_teacher_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='otp',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='otp',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]