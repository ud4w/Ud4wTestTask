# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'udaw_test_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(1985, 10, 26, 0, 0))),
            ('bio', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('jabber_id', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('skype_id', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('other_contacts', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'udaw_test', ['Person'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'udaw_test_person')


    models = {
        u'udaw_test.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(1985, 10, 26, 0, 0)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber_id': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'skype_id': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'})
        }
    }

    complete_apps = ['udaw_test']