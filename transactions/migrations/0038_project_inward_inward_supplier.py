# Generated by Django 4.1.5 on 2024-12-12 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0037_project_inward_inward_item_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_inward',
            name='inward_supplier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='transactions.inward_supplier'),
            preserve_default=False,
        ),
    ]
