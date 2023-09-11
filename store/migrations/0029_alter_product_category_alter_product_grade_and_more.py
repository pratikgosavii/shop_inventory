# Generated by Django 4.1.5 on 2023-09-07 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_alter_size_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='grade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.grade'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='shelf',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.godown'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.size'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='thickness',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.thickness'),
            preserve_default=False,
        ),
    ]