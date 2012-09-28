from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13, blank=True)

    def __unicode__(self):
        return self.name
