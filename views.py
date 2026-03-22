from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template import loader
#from geo_init.forms import MyGeoForm, GeoForm
from . import views
#from .models import States
import folium
#from basal_and_bark import basal_and_bark_folium as basal
import geopandas as gpd
import ee
from IPython.display import display

def home(request):
    return render(request, "home.html")

