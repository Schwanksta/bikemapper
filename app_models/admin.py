from django.contrib.gis import admin
from models import BikePath

class BikePathAdmin(admin.OSMGeoAdmin):
    list_display = ("user", "date_time")
    list_filter = ('user',)
admin.site.register(BikePath, BikePathAdmin)
