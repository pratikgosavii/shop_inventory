# Generated by Django 4.1.5 on 2024-08-30 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0018_project_matarial_production_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_inward',
            name='project',
        ),
        migrations.AddField(
            model_name='project_inward',
            name='customer',
            field=models.CharField(default='sdsd', max_length=50),
            preserve_default=False,
        ),
    ]
