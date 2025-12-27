from django.urls import path,include
from dataentry.views import import_data, export_data

urlpatterns = [
    path('import-data/', view=import_data, name="import_data"),
    path('export-data/', view=export_data, name="export_data"),
]
