# Generated by Django 5.1.4 on 2025-01-12 23:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0004_alter_psi_color_alter_psi_etching_alter_psi_text'),
        ('store', '0004_item_code_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psi',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
        migrations.AlterField(
            model_name='psi',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotation.color'),
        ),
        migrations.AlterField(
            model_name='psi',
            name='etching',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotation.etching'),
        ),
        migrations.AlterField(
            model_name='psi',
            name='text',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotation.text'),
        ),
        migrations.AlterField(
            model_name='psi',
            name='thickness',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.thickness'),
        ),
        migrations.AlterUniqueTogether(
            name='psi',
            unique_together={('category', 'thickness', 'etching', 'color', 'text')},
        ),
    ]
