# Generated by Django 4.1.5 on 2023-09-11 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0029_alter_product_category_alter_product_grade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='shelf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.godown'),
        ),
    ]
