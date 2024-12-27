# Generated by Django 5.1.4 on 2024-12-22 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0042_project_outward_main_label_sr_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_outward',
            name='main_label',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='transactions.project_outward_main_label'),
        ),
        migrations.AddField(
            model_name='project_outward_main_label',
            name='invoice_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project_outward_main_label',
            name='project_matarial_production',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outward_item_code_main_label', to='transactions.project_matarial_production'),
        ),
    ]
