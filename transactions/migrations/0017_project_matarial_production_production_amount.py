# Generated by Django 4.1.5 on 2024-08-23 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0016_rename_rra_invoice_project_rra_invoice_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_matarial_production',
            name='production_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
