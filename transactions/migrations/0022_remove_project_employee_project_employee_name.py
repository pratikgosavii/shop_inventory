# Generated by Django 4.1.5 on 2023-08-24 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_product_qr_date_of_pur'),
        ('transactions', '0021_remove_project_employee_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='employee',
        ),
        migrations.AddField(
            model_name='project',
            name='employee_name',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='dfsdds', to='store.employee'),
            preserve_default=False,
        ),
    ]
