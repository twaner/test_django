# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Contact_Information'
        db.delete_table(u'contact_contact_information')


    def backwards(self, orm):
        # Adding model 'Contact_Information'
        db.create_table(u'contact_contact_information', (
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(related_name='publisher_contact', to=orm['books.Publisher'])),
            (u'publisher_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['books.Publisher'], unique=True)),
            ('contact', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'contact', ['Contact_Information'])


    models = {
        
    }

    complete_apps = ['contact']