# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Item', fields ['list', 'text']
        db.create_unique(u'list_item', ['list_id', 'text'])

        # Adding field 'List.owner'
        db.add_column(u'list_list', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.User'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Removing unique constraint on 'Item', fields ['list', 'text']
        db.delete_unique(u'list_item', ['list_id', 'text'])

        # Deleting field 'List.owner'
        db.delete_column(u'list_list', 'owner_id')


    models = {
        u'accounts.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        u'list.item': {
            'Meta': {'ordering': "('id',)", 'unique_together': "(('list', 'text'),)", 'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['list.List']"}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        u'list.list': {
            'Meta': {'object_name': 'List'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.User']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['list']