# Generated by Django 4.1.7 on 2023-04-05 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0003_univ_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='univ_result',
            old_name='sem1',
            new_name='sem01',
        ),
        migrations.RenameField(
            model_name='univ_result',
            old_name='sem2',
            new_name='sem02',
        ),
        migrations.RenameField(
            model_name='univ_result',
            old_name='sem3',
            new_name='sem03',
        ),
        migrations.RenameField(
            model_name='univ_result',
            old_name='sem4',
            new_name='sem04',
        ),
        migrations.RenameField(
            model_name='univ_result',
            old_name='sem5',
            new_name='sem05',
        ),
        migrations.RenameField(
            model_name='univ_result',
            old_name='sem6',
            new_name='sem06',
        ),
        migrations.RenameField(
            model_name='univ_result',
            old_name='sem7',
            new_name='sem07',
        ),
        migrations.RenameField(
            model_name='univ_result',
            old_name='sem8',
            new_name='sem08',
        ),
    ]
