# Generated by Django 4.1.5 on 2024-12-11 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0031_project_matarial_production_barcode_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_outward',
            name='date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
