# Generated by Django 4.1.5 on 2023-07-28 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_alter_project_material_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_material',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_material_re', to='transactions.project'),
        ),
    ]
