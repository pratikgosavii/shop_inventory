# Generated by Django 5.1.4 on 2025-01-18 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0047_remove_order_customer_remove_order_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_inward',
            name='description',
            field=models.CharField(default='NA', max_length=500),
            preserve_default=False,
        ),
    ]
