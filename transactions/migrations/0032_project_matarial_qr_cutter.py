# Generated by Django 4.1.5 on 2023-09-01 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_cutter'),
        ('transactions', '0031_rename_customer_name_project_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_matarial_qr',
            name='cutter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.cutter'),
        ),
    ]
