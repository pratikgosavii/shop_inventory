# Generated by Django 4.1.5 on 2023-09-15 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0038_alter_shelf_name'),
        ('transactions', '0036_project_material_sheet_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_matarial_qr',
            name='product_qr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_qr_pro', to='store.product_qr'),
        ),
    ]
