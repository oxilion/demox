from djangorestframework.resources import ModelResource
from djangorestframework.reverse import reverse

from . import models


class Customer(ModelResource):
    model = models.Customer
    include = ('url',)

    def url(self, instance):
        return reverse('customer:api:customers:detail', args=[instance.pk],
                request=self.request)
