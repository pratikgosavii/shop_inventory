# Generated by Django 4.1.5 on 2024-12-13 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_qr_moved_to_left_over_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='inward_supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
