# Generated by Django 4.1.5 on 2023-10-22 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0043_employee_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.FloatField(default=0, unique=True),
        ),
    ]
