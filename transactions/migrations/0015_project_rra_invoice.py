# Generated by Django 4.1.5 on 2024-08-21 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0014_remove_project_inward_invoice_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='rra_invoice',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]