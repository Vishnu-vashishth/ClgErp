# Generated by Django 4.1.7 on 2023-04-02 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0009_alter_student_otp_alter_teacher_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='otp',
            field=models.CharField(blank=True, default=None, max_length=6, null=True),
        ),
    ]