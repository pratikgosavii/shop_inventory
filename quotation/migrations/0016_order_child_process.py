# Generated by Django 5.1.4 on 2025-01-28 20:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0015_remove_order_child_process'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_child',
            name='process',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sfdsddsds', to='quotation.process'),
        ),
    ]
