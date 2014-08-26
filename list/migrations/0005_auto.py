# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field shared_with on 'List'
        m2m_table_name = db.shorten_name(u'list_list_shared_with')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('list', models.ForeignKey(orm[u'list.list'], null=False)),
            ('user', models.ForeignKey(orm[u'accounts.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['list_id', 'user_id'])


    def backwards(self, orm):
        # Removing M2M table for field shared_with on 'List'
        db.delete_table(db.shorten_name(u'list_list_shared_with'))


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
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.User']", 'null': 'True', 'blank': 'True'}),
            'shared_with': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'users'", 'symmetrical': 'False', 'to': u"orm['accounts.User']"})
        }
    }

    complete_apps = ['list']