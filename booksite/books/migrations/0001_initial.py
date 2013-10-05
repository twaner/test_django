# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Publisher'
        db.create_table(u'books_publisher', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('state_province', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'books', ['Publisher'])

        # Adding model 'Author'
        db.create_table(u'books_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
        ))
        db.send_create_signal(u'books', ['Author'])

        # Adding model 'Book'
        db.create_table(u'books_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['books.Publisher'])),
            ('publication_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('num_pages', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'books', ['Book'])

        # Adding M2M table for field authors on 'Book'
        m2m_table_name = db.shorten_name(u'books_book_authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'books.book'], null=False)),
            ('author', models.ForeignKey(orm[u'books.author'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'author_id'])

        # Adding model 'HorrorBook'
        db.create_table(u'books_horrorbook', (
            (u'book_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['books.Book'], unique=True, primary_key=True)),
            ('how_scary', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'books', ['HorrorBook'])

        # Adding model 'TerrorBook'
        db.create_table(u'books_terrorbook', (
            (u'horrorbook_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['books.HorrorBook'], unique=True, primary_key=True)),
            ('test', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'books', ['TerrorBook'])

        # Adding model 'GhostWriter'
        db.create_table(u'books_ghostwriter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_f', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('name_l', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('num_books', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
        ))
        db.send_create_signal(u'books', ['GhostWriter'])


    def backwards(self, orm):
        # Deleting model 'Publisher'
        db.delete_table(u'books_publisher')

        # Deleting model 'Author'
        db.delete_table(u'books_author')

        # Deleting model 'Book'
        db.delete_table(u'books_book')

        # Removing M2M table for field authors on 'Book'
        db.delete_table(db.shorten_name(u'books_book_authors'))

        # Deleting model 'HorrorBook'
        db.delete_table(u'books_horrorbook')

        # Deleting model 'TerrorBook'
        db.delete_table(u'books_terrorbook')

        # Deleting model 'GhostWriter'
        db.delete_table(u'books_ghostwriter')


    models = {
        u'books.author': {
            'Meta': {'object_name': 'Author'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'books.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['books.Author']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_pages': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'publication_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['books.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'books.ghostwriter': {
            'Meta': {'object_name': 'GhostWriter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_f': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name_l': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'num_books': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'books.horrorbook': {
            'Meta': {'object_name': 'HorrorBook', '_ormbases': [u'books.Book']},
            u'book_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['books.Book']", 'unique': 'True', 'primary_key': 'True'}),
            'how_scary': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
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
        u'books.terrorbook': {
            'Meta': {'object_name': 'TerrorBook', '_ormbases': [u'books.HorrorBook']},
            u'horrorbook_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['books.HorrorBook']", 'unique': 'True', 'primary_key': 'True'}),
            'test': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['books']