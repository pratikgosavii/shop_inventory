# Generated by Django 4.1.5 on 2023-09-14 07:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0031_remove_product_shelf_remove_product_qr_shelf'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_qr',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
