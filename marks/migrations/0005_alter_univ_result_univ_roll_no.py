# Generated by Django 4.1.7 on 2023-04-05 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0004_alter_univ_result_univ_roll_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='univ_result',
            name='univ_roll_no',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]