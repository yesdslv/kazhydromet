# Generated by Django 3.0.4 on 2020-03-08 19:49

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0002_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hydrostation',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('nameEn', models.CharField(blank=True, max_length=255)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.Region')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
