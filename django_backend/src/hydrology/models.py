from django.contrib.gis.db import models

from common.models import Station


class HydrostationCategory(models.Model):
    code = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.code} {self.name}'


class Hydrostation(Station):
    category = models.ForeignKey(HydrostationCategory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


