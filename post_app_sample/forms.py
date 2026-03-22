from django import forms

#These forms are defined for uploading data to a map and to a table.
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    zoning_code = forms.CharField(max_length=50)
    geometry_code = forms.CharField(max_length=50)
    file = forms.FileField()

class UploadFileFormMap(forms.Form):
    title = forms.CharField(max_length=50)
    #zoning_code = forms.CharField(max_length=50)
    #geometry_code = forms.CharField(max_length=50)
    file = forms.FileField()