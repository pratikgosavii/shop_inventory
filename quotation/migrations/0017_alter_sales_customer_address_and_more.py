# Generated by Django 5.1.4 on 2025-02-05 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0016_order_child_process'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales_customer',
            name='address',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='sales_customer',
            name='client_gst',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='sales_customer',
            name='credit_limit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sales_customer',
            name='mobile_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
