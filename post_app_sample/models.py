#from django.db import models

# Create your models here.
from django.contrib.gis.db import models
#from django.db import models

#This is a test model
class NonGeoTest(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()

    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    #mpoly = models.MultiPolygonField()

#This is a test model with a multipolygon field
class GeoTest(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()


#This is the model that will be used for the form and everything else in this app.

class KnoxZoning(models.Model):
    zoning = models.CharField(max_length=50)
    geom = models.GeometryField()

    #geom = models.PolygonField()
    #geom = models.MultiPolygonField()