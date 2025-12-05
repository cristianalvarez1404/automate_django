from django.urls import path,include
from dataentry.views import import_data

urlpatterns = [
    path('import-data/', view=import_data, name="import_data")
]
