# Generated by Django 5.1.4 on 2025-01-28 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0014_alter_psi_unique_together_psi_process_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_child',
            name='process',
        ),
    ]
