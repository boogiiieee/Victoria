# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table(u'video_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(default='URL', max_length=100)),
            ('title_embed', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('video_url', self.gf('embed_video.fields.EmbedVideoField')(max_length=200)),
            ('title_file', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('file', self.gf('video.fields.VideoField')(max_length=100, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'video', ['Item'])


    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table(u'video_item')


    models = {
        u'video.item': {
            'Meta': {'ordering': "['sort', 'id']", 'object_name': 'Item'},
            'category': ('django.db.models.fields.CharField', [], {'default': "'URL'", 'max_length': '100'}),
            'file': ('video.fields.VideoField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title_embed': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title_file': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'video_url': ('embed_video.fields.EmbedVideoField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['video']