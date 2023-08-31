# Generated by Django 4.1.5 on 2023-08-31 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_remove_grade_category_remove_size_category_and_more'),
        ('transactions', '0029_project_matarial_qr_item_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='customer',
        ),
        migrations.AddField(
            model_name='project',
            name='customer_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='hfghjgjvhj', to='store.customer'),
            preserve_default=False,
        ),
    ]