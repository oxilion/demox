from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class PhoneNumber(models.Model):
    customer = models.ForeignKey(Customer)
    number = models.CharField(max_length=13)

    def __unicode__(self):
        return self.number

    class Meta:
        unique_together = ('customer', 'number')
