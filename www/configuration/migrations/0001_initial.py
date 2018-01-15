# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ConfigModel'
        db.create_table(u'configuration_configmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default=u'\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0430\u0439\u0442\u0430', max_length=100)),
            ('slogan', self.gf('django.db.models.fields.CharField')(default=u'\u0421\u043b\u043e\u0433\u0430\u043d \u0441\u0430\u0439\u0442\u0430', max_length=100)),
        ))
        db.send_create_signal(u'configuration', ['ConfigModel'])


    def backwards(self, orm):
        # Deleting model 'ConfigModel'
        db.delete_table(u'configuration_configmodel')


    models = {
        u'configuration.configmodel': {
            'Meta': {'object_name': 'ConfigModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slogan': ('django.db.models.fields.CharField', [], {'default': "u'\\u0421\\u043b\\u043e\\u0433\\u0430\\u043d \\u0441\\u0430\\u0439\\u0442\\u0430'", 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'\\u041d\\u0430\\u0437\\u0432\\u0430\\u043d\\u0438\\u0435 \\u0441\\u0430\\u0439\\u0442\\u0430'", 'max_length': '100'})
        }
    }

    complete_apps = ['configuration']