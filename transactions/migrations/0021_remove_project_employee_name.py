# Generated by Django 4.1.5 on 2023-08-24 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0020_alter_left_over_stock_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='employee_name',
        ),
    ]
