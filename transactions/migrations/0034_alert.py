# Generated by Django 4.1.5 on 2023-09-09 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0033_remove_project_matarial_qr_is_work_done_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
