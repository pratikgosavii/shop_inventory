# Generated by Django 4.1.5 on 2023-12-16 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0054_remove_project_logs_description_project_sheets_logs'),
    ]

    operations = [
        migrations.CreateModel(
            name='notification_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
