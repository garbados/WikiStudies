# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'User'
        db.create_table('study_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('pw', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('join_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('auth', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal('study', ['User'])

        # Adding model 'Study'
        db.create_table('study_study', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('study', ['Study'])

        # Adding model 'Author'
        db.create_table('study_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('study', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['study.Study'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['study.User'])),
        ))
        db.send_create_signal('study', ['Author'])

        # Adding model 'Section'
        db.create_table('study_section', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('study', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['study.Study'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('study', ['Section'])

        # Adding model 'Comment'
        db.create_table('study_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['study.Section'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['study.User'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('study', ['Comment'])

        # Adding model 'Review'
        db.create_table('study_review', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('study', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['study.Study'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['study.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('save', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('study', ['Review'])

        # Adding model 'Tag'
        db.create_table('study_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('study', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['study.Study'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('study', ['Tag'])

        # Adding model 'Citation'
        db.create_table('study_citation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('study', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Citer', to=orm['study.Study'])),
            ('cite', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Cited', to=orm['study.Study'])),
        ))
        db.send_create_signal('study', ['Citation'])

        # Adding model 'Vote'
        db.create_table('study_vote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('study', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['study.Study'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['study.User'])),
            ('vote', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('study', ['Vote'])

        # Adding model 'ReportStudy'
        db.create_table('study_reportstudy', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('study', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['study.Study'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['study.User'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal('study', ['ReportStudy'])

        # Adding model 'ReportSection'
        db.create_table('study_reportsection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['study.Section'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['study.User'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal('study', ['ReportSection'])

        # Adding model 'ReportReview'
        db.create_table('study_reportreview', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('review', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['study.Review'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['study.User'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal('study', ['ReportReview'])

        # Adding model 'ReportComment'
        db.create_table('study_reportcomment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['study.Comment'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['study.User'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal('study', ['ReportComment'])


    def backwards(self, orm):
        
        # Deleting model 'User'
        db.delete_table('study_user')

        # Deleting model 'Study'
        db.delete_table('study_study')

        # Deleting model 'Author'
        db.delete_table('study_author')

        # Deleting model 'Section'
        db.delete_table('study_section')

        # Deleting model 'Comment'
        db.delete_table('study_comment')

        # Deleting model 'Review'
        db.delete_table('study_review')

        # Deleting model 'Tag'
        db.delete_table('study_tag')

        # Deleting model 'Citation'
        db.delete_table('study_citation')

        # Deleting model 'Vote'
        db.delete_table('study_vote')

        # Deleting model 'ReportStudy'
        db.delete_table('study_reportstudy')

        # Deleting model 'ReportSection'
        db.delete_table('study_reportsection')

        # Deleting model 'ReportReview'
        db.delete_table('study_reportreview')

        # Deleting model 'ReportComment'
        db.delete_table('study_reportcomment')


    models = {
        'study.author': {
            'Meta': {'object_name': 'Author'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['study.Study']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['study.User']"})
        },
        'study.citation': {
            'Meta': {'object_name': 'Citation'},
            'cite': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Cited'", 'to': "orm['study.Study']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Citer'", 'to': "orm['study.Study']"})
        },
        'study.comment': {
            'Meta': {'object_name': 'Comment'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['study.Section']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['study.User']"})
        },
        'study.reportcomment': {
            'Meta': {'object_name': 'ReportComment'},
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['study.Comment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['study.User']"})
        },
        'study.reportreview': {
            'Meta': {'object_name': 'ReportReview'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'review': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['study.Review']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['study.User']"})
        },
        'study.reportsection': {
            'Meta': {'object_name': 'ReportSection'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['study.Section']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['study.User']"})
        },
        'study.reportstudy': {
            'Meta': {'object_name': 'ReportStudy'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['study.Study']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['study.User']"})
        },
        'study.review': {
            'Meta': {'object_name': 'Review'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'save': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['study.Study']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['study.User']"})
        },
        'study.section': {
            'Meta': {'object_name': 'Section'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['study.Study']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'study.study': {
            'Meta': {'object_name': 'Study'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'study.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['study.Study']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'study.user': {
            'Meta': {'object_name': 'User'},
            'auth': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'join_date': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'pw': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'study.vote': {
            'Meta': {'object_name': 'Vote'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['study.Study']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['study.User']"}),
            'vote': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['study']
