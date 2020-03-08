from django.db import migrations
from django.contrib.gis.geos import fromstr

from hydrology.initial_data import hydrostations


def fill_hydrostations_initial_data(apps, schema_editor):
    Hydrostation = apps.get_model('hydrology', 'Hydrostation')
    HydrostationCategory = apps.get_model('hydrology', 'HydrostationCategory')
    Region = apps.get_model('common', 'Region')
    for hydrostation in hydrostations:
        region = Region.objects.get(code=hydrostation['region'])
        hydrostation_category = HydrostationCategory.objects.get(code=hydrostation['category'])
        lat = hydrostation['lat']
        lon = hydrostation['lon']
        Hydrostation.objects.create(
            code=hydrostation['pk'],
            name=hydrostation['name'],
            nameEn=hydrostation['nameEn'],
            region=region,
            category=hydrostation_category,
            location=fromstr(f'POINT({lon} {lat})', srid=4326)
        )


def delete_hydrostations_initial_data(apps, schema_editor):
    Hydrostation = apps.get_model('hydrology', 'Hydrostation')
    Hydrostation.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('hydrology', '0003_hydrostation_category_initial_data'),
        ('common', '0003_fill_initial_region_data'),
    ]

    operations = [
        migrations.RunPython(fill_hydrostations_initial_data, delete_hydrostations_initial_data)
    ]