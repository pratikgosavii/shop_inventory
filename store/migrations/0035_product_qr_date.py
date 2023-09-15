# Generated by Django 4.1.5 on 2023-09-15 09:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0034_remove_product_qr_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_qr',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]