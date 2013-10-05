# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact_Information'
        db.create_table(u'contact_contact_information', (
            (u'publisher_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['books.Publisher'], unique=True)),
            ('contact', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(related_name='publisher_contact', to=orm['books.Publisher'])),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'contact', ['Contact_Information'])


    def backwards(self, orm):
        # Deleting model 'Contact_Information'
        db.delete_table(u'contact_contact_information')


    models = {
        u'books.publisher': {
            'Meta': {'ordering': "['name']", 'object_name': 'Publisher'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'state_province': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'contact.contact_information': {
            'Meta': {'ordering': "['name']", 'object_name': 'Contact_Information', '_ormbases': [u'books.Publisher']},
            'contact': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'publisher_contact'", 'to': u"orm['books.Publisher']"}),
            u'publisher_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['books.Publisher']", 'unique': 'True'})
        }
    }

    complete_apps = ['contact']