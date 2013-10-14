from django.contrib.gis import admin
from models import BikePath

class BikePathAdmin(admin.OSMGeoAdmin):
    list_display = ('user', 'approved', 'rating', 'date_time',)
    list_filter = ('user', 'approved', 'rating')
admin.site.register(BikePath, BikePathAdmin)
