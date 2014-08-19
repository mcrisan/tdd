# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'List'
        db.create_table(u'list_list', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'list', ['List'])

        # Adding field 'Item.list'
        db.add_column(u'list_item', 'list',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['list.List']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'List'
        db.delete_table(u'list_list')

        # Deleting field 'Item.list'
        db.delete_column(u'list_item', 'list_id')


    models = {
        u'list.item': {
            'Meta': {'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['list.List']"}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        u'list.list': {
            'Meta': {'object_name': 'List'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['list']