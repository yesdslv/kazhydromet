from django.contrib.gis.db import models


class Region(models.Model):
    code = models.CharField(primary_key=True, max_length=31)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'regions'


class Station(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    nameEn = models.CharField(max_length=255, blank=True)
    location = models.PointField()
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True
