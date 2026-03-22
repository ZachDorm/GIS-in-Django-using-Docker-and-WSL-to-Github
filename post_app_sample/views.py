#This file contains most of the backend communication. 
# It is this file, coupled with the urls.py file, that 
# allows for proper management of information submitted 
# to a form and redirecting to a new location where the 
# result of the uploaded information is shown to the user.
#If interested, you can toggle between the two files and 
# see how they communicate to one another with the functions below.

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm, UploadFileFormMap
from .models import KnoxZoning
import folium

from django.contrib.gis.geos import Polygon, MultiPolygon

import geopandas as gpd
import pandas as pd
# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            table = handle_uploaded_file(request.FILES["file"])
            zone_field = form.cleaned_data['zoning_code']
            geom_field = form.cleaned_data['geometry_code']
            save_in_model_knox_zoning(zone_field, table[geom_field].to_wkt())
            #return HttpResponseRedirect("/success/url/")
            return HttpResponse(table.to_html())
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})


def handle_uploaded_file(file):
    shp = gpd.read_file(file, rows=slice(1,10000), encoding='utf-8')
    return shp
    #print(pd.DataFrame(shp))
    #return pd.DataFrame(shp)

def table(request):
    #if request.method == "POST":
    #    form = UploadFileForm(request.POST, request.FILES)
    #    if form.is_valid():
            table = handle_uploaded_file(request)#.FILES["file"])
            #return HttpResponseRedirect("/success/url/")
            return HttpResponse(table.to_html())
from django.contrib.gis.geos import GEOSGeometry
def save_in_model_knox_zoning(zone_field, geom_field):
    count = 0
    for i in zone_field:
         my_object = KnoxZoning.objects.create(zoning=zone_field[count], geom=GEOSGeometry(geom_field[count]))
         count = count +1
        #my_object = KnoxZoning.objects.create(zoning=zone_field[1], geom=GEOSGeometry(geom_field[1]))


def show_map(request):
    m = folium.Map([30,-100], zoom_start=10)
    print(type(m))
    figure = folium.Figure()
    #ee.Authenticate()
    #ee.Initialize()
    #dem = ee.Image("UMD/hansen/global_forest_change_2023_v1_11").select('treecover2000')
    vis_params = {
        'min': 0,
        'max':4000,
        'palette':['006633', 'E5FFCC', 'D8D8D8', 'F5F5F5']
    }

    #obj = States.objects.get(NAME=i).mpoly#.geojson

    #dem_add = dem.reproject(crs=ee.Projection('EPSG:4326'), scale=1000)
    #dem_add=dem
    
    #map_id_dict = dem.getMapId(vis_params)
    #new_m = folium.raster_layers.TileLayer(
    #    tiles = map_id_dict['tile_fetcher'].url_format,
    #    attr ='Google Earth Engine',
    #    name="test",
    #    overlay=True,
    #    control=True
    #)

    #new_m.add_to(m)

    m.add_child(folium.LayerControl())
    #m_dis = m.save("geo_init/templates/geo_init/test.html")
    context = {'map':m,}

    return render(request, 'geemapping.html', context)



def upload_file_map(request):
    if request.method == "POST":
        form = UploadFileFormMap(request.POST, request.FILES)
        if form.is_valid():
            table = handle_uploaded_file(request.FILES["file"])
            #zone_field = form.cleaned_data['zoning_code']
            #geom_field = form.cleaned_data['geometry_code']
            #save_in_model_knox_zoning(zone_field, table[geom_field].to_wkt())
            
            #return HttpResponseRedirect("/success/url/")
            #return HttpResponse(table.explore()._repr_html_())#.to_html())

            map_html = table.explore()._repr_html_()
    
            context = {'map_html': map_html}

            return render(request, 'exploremap.html', context)
            #return HttpResponse(table[geom_field].to_html())

    else:
        form = UploadFileForm()
    return render(request, "uploadmap.html", {"form": form})

def map_view(request):
    # Example: Create a simple GeoDataFrame
    df = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    
    # Generate the map
    m = df.explore()
    
    # Get HTML representation
    map_html = m._repr_html_()
    
    context = {'map_html': map_html}
    return render(request, 'map_template.html', context)