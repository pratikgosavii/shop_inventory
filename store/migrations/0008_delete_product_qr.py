# Generated by Django 4.1.5 on 2023-07-29 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_product_qr_code_remove_product_shelf_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='product_qr',
        ),
    ]
