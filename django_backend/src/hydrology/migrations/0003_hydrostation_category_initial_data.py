from django.db import migrations

from hydrology.initial_data import hydrostation_categories


def fill_hydrostation_category_initial_data(apps, schema_editor):
    HydrostationCategory = apps.get_model('hydrology', 'HydrostationCategory')
    for category in hydrostation_categories:
        HydrostationCategory.objects.create(code=category['pk'], name=category['name'])


def delete_hydrostation_category_initial_data(apps, schema_editor):
    HydrostationCategory = apps.get_model('hydrology', 'HydrostationCategory')
    HydrostationCategory.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('hydrology', '0002_auto_20200308_2025'),
    ]

    operations = [
        migrations.RunPython(fill_hydrostation_category_initial_data, delete_hydrostation_category_initial_data)
    ]
