# Generated by Django 4.1.5 on 2024-02-11 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0063_rename_desgin_file_project_design_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='own_design_file',
            field=models.FileField(blank=True, upload_to='media/project_design/'),
        ),
    ]
