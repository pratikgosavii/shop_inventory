# Generated by Django 4.1.5 on 2023-10-27 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0044_alter_size_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('size', 'category', 'thickness', 'grade')},
        ),
    ]