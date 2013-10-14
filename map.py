from importd import d
from django.conf.urls import include

from settings import DATABASES, INSTALLED_APPS, STATIC_URL
d(DEBUG = True,
    DATABASES = DATABASES,
    STATIC_URL = STATIC_URL,
    INSTALLED_APPS = INSTALLED_APPS)

from django.contrib.gis.geos import GEOSGeometry, MultiLineString, LineString
from django.contrib import admin
admin.autodiscover()
d.urlpatterns += d.patterns('', d.url(r'^admin/', include(admin.site.urls)))

from app_models.models import BikePath

@d("^$", name="index")
def index(request):
    paths = BikePath.objects.filter(approved=True).geojson()
    return "index.html", {
        "paths": paths.geojson,
        "rating_choices": BikePath.RATING_CHOICES
    }

@d
def submit(request):
    if request.method != 'POST':
        return d.Http404
    data = request.POST
    user = "test@test.com"
    geom = GEOSGeometry(data.get('json'))
    path = MultiLineString([LineString(line) for line in geom.tuple])
    comment = data.get('comment')
    bp = BikePath(
        user=user,
        rating=int(data.get('rating')),
        path=path,
        comment=comment
    )
    bp.save()
    return d.HttpResponse("OK")
