# Generated by Django 4.1.5 on 2024-12-12 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0038_project_inward_inward_supplier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_inward',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='project_inward',
            name='description',
        ),
    ]
