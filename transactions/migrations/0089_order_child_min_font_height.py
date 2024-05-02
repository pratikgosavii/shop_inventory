# Generated by Django 4.1.5 on 2024-04-26 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0088_remove_order_client_gst_order_child_final_item_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_child',
            name='min_font_height',
            field=models.CharField(choices=[('1mm', '1mm'), ('600mm', '600mm')], default='1mm', max_length=50),
            preserve_default=False,
        ),
    ]