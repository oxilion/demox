from djangorestframework.resources import ModelResource
from djangorestframework.reverse import reverse

from . import models


class Customer(ModelResource):
    model = models.Customer
    include = ('phone_numbers', 'url')

    def phone_numbers(self, instance):
        return reverse('customer:api:customers:phone_numbers',
                args=[instance.pk], request=self.request)

    def url(self, instance):
        return reverse('customer:api:customers:detail', args=[instance.pk],
                request=self.request)


class PhoneNumber(ModelResource):
    model = models.PhoneNumber
    fields = ('customer', 'number', 'url')

    def url(self, instance):
        return reverse('customer:api:customers:phone_number',
                args=[instance.customer.pk, instance.number],
                request=self.request)
