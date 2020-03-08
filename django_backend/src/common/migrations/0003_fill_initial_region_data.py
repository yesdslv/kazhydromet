from django.db import migrations

from common.initial_data import regions


def fill_region_initial_data(apps, schema_editor):
    Region = apps.get_model('common', 'Region')
    for region in regions:
        Region.objects.create(code=region['pk'], name=region['name'])


def delete_region_initial_data(apps, schema_editor):
    Region = apps.get_model('common', 'Region')
    Region.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_region'),
    ]

    operations = [
        migrations.RunPython(fill_region_initial_data, delete_region_initial_data)
    ]
