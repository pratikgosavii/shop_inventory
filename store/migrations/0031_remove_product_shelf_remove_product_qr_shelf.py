# Generated by Django 4.1.5 on 2023-09-12 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0030_alter_product_shelf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='shelf',
        ),
        migrations.RemoveField(
            model_name='product_qr',
            name='shelf',
        ),
    ]
