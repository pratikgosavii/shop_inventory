# Generated by Django 4.1.5 on 2024-04-28 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0090_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_sqinch',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
