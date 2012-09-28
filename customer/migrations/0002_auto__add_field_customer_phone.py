# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Customer.phone'
        db.add_column('customer_customer', 'phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=13, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Customer.phone'
        db.delete_column('customer_customer', 'phone')


    models = {
        'customer.customer': {
            'Meta': {'object_name': 'Customer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '13', 'blank': 'True'})
        }
    }

    complete_apps = ['customer']