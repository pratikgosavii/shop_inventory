# Generated by Django 4.1.5 on 2024-02-11 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0062_project_desgin_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='desgin_file',
            new_name='design_file',
        ),
    ]
