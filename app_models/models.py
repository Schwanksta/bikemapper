from django.contrib.gis.db import models

class BikePath(models.Model):
    user = models.CharField(max_length=255)
    comment = models.TextField()
    date_time = models.DateTimeField()
    path = models.PolygonField(srid=900913)

    objects= models.GeoManager()

    def __str__(self):
        return u"%s @ %s" % (self.user, self.date_time)
    
    def save(self, *args, **kwargs):
        if not date_time:
            date_time = datetime.now()
        super(BikePath, self).save(*args, **kwargs)
