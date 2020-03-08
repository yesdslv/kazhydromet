from django.contrib.gis.db import models


class Region(models.Model):
    code = models.CharField(primary_key=True, max_length=31)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'regions'


class Station(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    region = models.ForeignKey(Region, on_delete=models.SET_NULL)

    class Meta:
        abstract = True
