# Generated by Django 4.1.5 on 2023-09-04 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_product_qr_uploaded_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_qr',
            name='uploaded_file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
