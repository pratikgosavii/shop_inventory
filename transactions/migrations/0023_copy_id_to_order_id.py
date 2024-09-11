from django.db import migrations

def copy_id_to_order_id(apps, schema_editor):
    Project = apps.get_model('transactions', 'project')
    for project in Project.objects.all():
        project.order_id = project.id
        project.save()

class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0022_alter_project_order_id'),
    ]

    operations = [
        migrations.RunPython(copy_id_to_order_id),
    ]
