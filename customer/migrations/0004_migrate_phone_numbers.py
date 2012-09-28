# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models


class Migration(DataMigration):

    def forwards(self, orm):
        for customer in orm['customer.Customer'].objects.exclude(phone=''):
            phone_number = orm['customer.Phonenumber']()
            phone_number.customer = customer
            phone_number.number = customer.phone
            phone_number.save()

            customer.phone = ''
            customer.save()

    def backwards(self, orm):
        for phone_number in orm['customer.Phonenumber'].objects.all():
            if not phone_number.customer.phone:
                phone_number.customer.phone = phone_number.number
                phone_number.customer.save()
                phone_number.delete()


    models = {
        'customer.customer': {
            'Meta': {'object_name': 'Customer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '13', 'blank': 'True'})
        },
        'customer.phonenumber': {
            'Meta': {'unique_together': "(('customer', 'number'),)", 'object_name': 'PhoneNumber'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['customer.Customer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '13'})
        }
    }


    complete_apps = ['customer']
    symmetrical = True
