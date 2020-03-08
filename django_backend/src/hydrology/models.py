from django.contrib.gis.db import models

from common.models import Station


class Hydrostation(Station):


    def __str__(self):
        return self.name

