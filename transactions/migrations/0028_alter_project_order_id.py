# Generated by Django 4.1.5 on 2024-09-20 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0027_alter_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='order_id',
            field=models.CharField(default='contact pratik', max_length=50, unique=True),
            preserve_default=False,
        ),
    ]