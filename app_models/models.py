from datetime import datetime
from django.contrib.gis.db import models

class BikePath(models.Model):
    user = models.CharField(max_length=255)
    RATING_CHOICES = (
        (1,'Good'),
        (2,'Usable'),
        (3,'Bad'),
    )
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    date_time = models.DateTimeField()
    path = models.MultiLineStringField(srid=4326)
    approved = models.BooleanField(default=False)

    objects= models.GeoManager()

    def __str__(self):
        return u"%s @ %s" % (self.user, self.date_time)
    
    def save(self, *args, **kwargs):
        if not self.date_time:
            self.date_time = datetime.now()
        super(BikePath, self).save(*args, **kwargs)
