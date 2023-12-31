# Generated by Django 4.1.5 on 2023-07-25 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_category_godown'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='godown',
            new_name='shelf',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='grade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.grade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='piece',
            field=models.IntegerField(default=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='thickness',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.thickness'),
            preserve_default=False,
        ),
    ]
