# Generated by Django 4.1.7 on 2023-04-02 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_student_curent_sem_alter_agg_attendance_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('otp', models.IntegerField(default=None, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='otp',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
