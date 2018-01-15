# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ConfigModel.slogan'
        db.delete_column(u'configuration_configmodel', 'slogan')

        # Adding field 'ConfigModel.code_phone'
        db.add_column(u'configuration_configmodel', 'code_phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10, blank=True),
                      keep_default=False)

        # Adding field 'ConfigModel.phone'
        db.add_column(u'configuration_configmodel', 'phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True),
                      keep_default=False)

        # Adding field 'ConfigModel.email'
        db.add_column(u'configuration_configmodel', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'ConfigModel.adress'
        db.add_column(u'configuration_configmodel', 'adress',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=300, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'ConfigModel.slogan'
        db.add_column(u'configuration_configmodel', 'slogan',
                      self.gf('django.db.models.fields.CharField')(default=u'\u0421\u043b\u043e\u0433\u0430\u043d \u0441\u0430\u0439\u0442\u0430', max_length=100),
                      keep_default=False)

        # Deleting field 'ConfigModel.code_phone'
        db.delete_column(u'configuration_configmodel', 'code_phone')

        # Deleting field 'ConfigModel.phone'
        db.delete_column(u'configuration_configmodel', 'phone')

        # Deleting field 'ConfigModel.email'
        db.delete_column(u'configuration_configmodel', 'email')

        # Deleting field 'ConfigModel.adress'
        db.delete_column(u'configuration_configmodel', 'adress')


    models = {
        u'configuration.configmodel': {
            'Meta': {'object_name': 'ConfigModel'},
            'adress': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'code_phone': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'\\u041d\\u0430\\u0437\\u0432\\u0430\\u043d\\u0438\\u0435 \\u0441\\u0430\\u0439\\u0442\\u0430'", 'max_length': '100'})
        }
    }

    complete_apps = ['configuration']