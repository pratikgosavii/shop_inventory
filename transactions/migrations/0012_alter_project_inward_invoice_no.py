# Generated by Django 4.1.5 on 2024-08-18 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0011_project_outward'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_inward',
            name='invoice_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
