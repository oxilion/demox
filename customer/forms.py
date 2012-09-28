from django.forms import ModelForm

from . import models


class PhoneNumber(ModelForm):
    class Meta:
        model = models.PhoneNumber
        exclude = ('customer',)
