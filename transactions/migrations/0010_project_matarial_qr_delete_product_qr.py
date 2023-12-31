# Generated by Django 4.1.5 on 2023-07-30 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0009_product_qr'),
    ]

    operations = [
        migrations.CreateModel(
            name='project_matarial_qr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='static/qrcode/')),
                ('project_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_material_re', to='transactions.project_material')),
            ],
        ),
        migrations.DeleteModel(
            name='product_qr',
        ),
    ]
