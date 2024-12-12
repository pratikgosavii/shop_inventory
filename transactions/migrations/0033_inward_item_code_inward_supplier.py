# Generated by Django 4.1.5 on 2024-12-12 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0032_project_outward_date_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='inward_item_code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_code', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='inward_supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_code', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
    ]
