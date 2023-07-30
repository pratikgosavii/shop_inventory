# Generated by Django 4.1.5 on 2023-07-25 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.BigIntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('godown', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sfwwfddfds', to='store.godown')),
            ],
        ),
        migrations.CreateModel(
            name='request_material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(blank=True, max_length=50, null=True)),
                ('bags', models.BigIntegerField()),
                ('DC_number', models.CharField(max_length=50)),
                ('DC_date', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dscdc', to='store.category')),
                ('customer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dscdc', to='store.customer')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sdcdscd', to='store.size')),
            ],
        ),
        migrations.CreateModel(
            name='inward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(blank=True, max_length=50, null=True)),
                ('bags', models.BigIntegerField()),
                ('DC_number', models.CharField(max_length=50)),
                ('DC_date', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wfgv', to='store.category')),
                ('godown', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sdwe', to='store.godown')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='xvc', to='store.size')),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DC_date', models.DateField()),
                ('description', models.CharField(max_length=50)),
                ('employee_name', models.CharField(max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dsscsdcs', to='store.customer')),
            ],
        ),
    ]
