from djangorestframework.reverse import reverse
from djangorestframework.views import (View, ListOrCreateModelView,
        InstanceModelView)

from . import forms
from . import resources


class Root(View):
    links = (
            ('customers', 'customer:api:customers:list'),
    )

    def get(self, request):
        return [{'name': name, 'url': reverse(url, request=request)} for name,
                url in self.links]


class CustomerList(ListOrCreateModelView):
    resource = resources.Customer


class CustomerInstance(InstanceModelView):
    resource = resources.Customer


class PhoneNumberList(ListOrCreateModelView):
    resource = resources.PhoneNumber
    form = forms.PhoneNumber


class PhoneNumberInstance(InstanceModelView):
    resource = resources.PhoneNumber
    form = forms.PhoneNumber
