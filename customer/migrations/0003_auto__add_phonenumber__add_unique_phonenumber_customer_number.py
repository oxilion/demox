# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PhoneNumber'
        db.create_table('customer_phonenumber', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['customer.Customer'])),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=13)),
        ))
        db.send_create_signal('customer', ['PhoneNumber'])

        # Adding unique constraint on 'PhoneNumber', fields ['customer', 'number']
        db.create_unique('customer_phonenumber', ['customer_id', 'number'])


    def backwards(self, orm):
        # Removing unique constraint on 'PhoneNumber', fields ['customer', 'number']
        db.delete_unique('customer_phonenumber', ['customer_id', 'number'])

        # Deleting model 'PhoneNumber'
        db.delete_table('customer_phonenumber')


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