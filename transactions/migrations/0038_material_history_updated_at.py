# Generated by Django 4.1.5 on 2023-09-17 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0037_alter_project_matarial_qr_product_qr'),
    ]

    operations = [
        migrations.AddField(
            model_name='material_history',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
