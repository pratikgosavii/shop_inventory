# Generated by Django 4.1.5 on 2024-08-21 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0015_project_rra_invoice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='rra_invoice',
            new_name='rra_invoice_no',
        ),
    ]