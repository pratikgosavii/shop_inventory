# Generated by Django 4.1.5 on 2024-02-13 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0066_sheets_rifd_remove_values_for_assignment_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='values_for_assignment',
            name='sheet_id',
            field=models.CharField(max_length=50),
        ),
    ]
