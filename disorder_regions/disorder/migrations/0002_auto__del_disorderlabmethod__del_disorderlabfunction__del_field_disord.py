# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Disorderlabmethod'
        db.delete_table(u'disorderlabmethod')

        # Deleting model 'Disorderlabfunction'
        db.delete_table(u'disorderlabfunction')

        # Deleting field 'Disorderlab.disorderlab_methodid_fr'
        db.delete_column(u'disorderlab', 'disorderLab_methodID_FR')

        # Deleting field 'Disorderlab.disorderlab_functionid_fr'
        db.delete_column(u'disorderlab', 'disorderLab_functionID_FR')

        # Deleting field 'Protein.protein_percentageofdisorder'
        db.delete_column(u'protein', 'protein_percentageOfDisorder')

        # Deleting field 'Proteinmutationdisease.proteinmutationdisease_description'
        db.delete_column(u'proteinmutationdisease', 'proteinMutationDisease_description')

        # Deleting field 'Individualpreresultmutprotein.individualpreresultmutprotein_uniprot_fr'
        db.delete_column(u'individualpreresultmutprotein', 'individualPreResultMutProtein_Uniprot_FR')


    def backwards(self, orm):
        
        # Adding model 'Disorderlabmethod'
        db.create_table(u'disorderlabmethod', (
            ('disorderlabmethod_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='disorderLabMethod_ID')),
            ('disorderlabmethod_description', self.gf('django.db.models.fields.TextField')(db_column='disorderLabMethod_description', blank=True)),
            ('disorderlabmethod_name', self.gf('django.db.models.fields.TextField')(db_column='disorderLabMethod_name')),
            ('disorderlabmethod_reference', self.gf('django.db.models.fields.TextField')(db_column='disorderLabMethod_reference', blank=True)),
        ))
        db.send_create_signal('disorder', ['Disorderlabmethod'])

        # Adding model 'Disorderlabfunction'
        db.create_table(u'disorderlabfunction', (
            ('disorderlabfunction_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='disorderLabFunction_ID')),
            ('disorderlabfunction_name', self.gf('django.db.models.fields.TextField')(db_column='disorderLabFunction_name')),
        ))
        db.send_create_signal('disorder', ['Disorderlabfunction'])

        # Adding field 'Disorderlab.disorderlab_methodid_fr'
        db.add_column(u'disorderlab', 'disorderlab_methodid_fr', self.gf('django.db.models.fields.related.ForeignKey')(default=datetime.date(2012, 2, 24), to=orm['disorder.Disorderlabmethod'], db_column='disorderLab_methodID_FR'), keep_default=False)

        # Adding field 'Disorderlab.disorderlab_functionid_fr'
        db.add_column(u'disorderlab', 'disorderlab_functionid_fr', self.gf('django.db.models.fields.related.ForeignKey')(default=datetime.date(2012, 2, 24), to=orm['disorder.Disorderlabfunction'], db_column='disorderLab_functionID_FR'), keep_default=False)

        # Adding field 'Protein.protein_percentageofdisorder'
        db.add_column(u'protein', 'protein_percentageofdisorder', self.gf('django.db.models.fields.DecimalField')(default='0%', decimal_places=3, db_column='protein_percentageOfDisorder', max_digits=7), keep_default=False)

        # Adding field 'Proteinmutationdisease.proteinmutationdisease_description'
        db.add_column(u'proteinmutationdisease', 'proteinmutationdisease_description', self.gf('django.db.models.fields.TextField')(default='', db_column='proteinMutationDisease_description', blank=True), keep_default=False)

        # Adding field 'Individualpreresultmutprotein.individualpreresultmutprotein_uniprot_fr'
        db.add_column(u'individualpreresultmutprotein', 'individualpreresultmutprotein_uniprot_fr', self.gf('django.db.models.fields.related.ForeignKey')(default=datetime.date(2012, 2, 24), to=orm['disorder.Protein'], db_column='individualPreResultMutProtein_Uniprot_FR'), keep_default=False)


    models = {
        'disorder.disorderlab': {
            'Meta': {'object_name': 'Disorderlab', 'db_table': "u'disorderlab'"},
            'disorderlab_end': ('django.db.models.fields.IntegerField', [], {'db_column': "'disorderLab_end'"}),
            'disorderlab_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'disorderLab_ID'"}),
            'disorderlab_proteinuniprot_fr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['disorder.Protein']", 'db_column': "'disorderLab_proteinUniprot_FR'"}),
            'disorderlab_sequence': ('django.db.models.fields.TextField', [], {'db_column': "'disorderLab_sequence'"}),
            'disorderlab_start': ('django.db.models.fields.IntegerField', [], {'db_column': "'disorderLab_start'"})
        },
        'disorder.disorderpredictorresults': {
            'Meta': {'object_name': 'Disorderpredictorresults', 'db_table': "u'disorderpredictorresults'"},
            'disorderpredictorresult_end': ('django.db.models.fields.IntegerField', [], {'db_column': "'disorderPredictorResult_end'"}),
            'disorderpredictorresult_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'disorderPredictorResult_ID'"}),
            'disorderpredictorresult_proteinid_fr': ('django.db.models.fields.IntegerField', [], {'db_column': "'disorderPredictorResult_proteinID_FR'"}),
            'disorderpredictorresult_sequence': ('django.db.models.fields.TextField', [], {'db_column': "'disorderPredictorResult_sequence'"}),
            'disorderpredictorresult_start': ('django.db.models.fields.IntegerField', [], {'db_column': "'disorderPredictorResult_start'"})
        },
        'disorder.individualpremutproteindisochange': {
            'Meta': {'object_name': 'Individualpremutproteindisochange', 'db_table': "u'individualpremutproteindisochange'"},
            'individualpremutproteindisochange_disorderchange': ('django.db.models.fields.CharField', [], {'max_length': '135', 'db_column': "'individualPreMutProteinDisoChange_disorderChange'"}),
            'individualpremutproteindisochange_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'individualPreMutProteinDisoChange_ID'"}),
            'individualpremutproteindisochange_mutaa': ('django.db.models.fields.CharField', [], {'max_length': '135', 'db_column': "'individualPreMutProteinDisoChange_mutAA'"}),
            'individualpremutproteindisochange_mutposition': ('django.db.models.fields.IntegerField', [], {'db_column': "'individualPreMutProteinDisoChange_mutPosition'"}),
            'individualpremutproteindisochange_mutproteinid_fr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['disorder.Mutprotein']", 'db_column': "'individualPreMutProteinDisoChange_mutProteinID_FR'"}),
            'individualpremutproteindisochange_mutscore': ('django.db.models.fields.DecimalField', [], {'db_column': "'individualPreMutProteinDisoChange_mutScore'", 'decimal_places': '3', 'max_digits': '8'}),
            'individualpremutproteindisochange_origaa': ('django.db.models.fields.CharField', [], {'max_length': '135', 'db_column': "'individualPreMutProteinDisoChange_origAA'"}),
            'individualpremutproteindisochange_origscore': ('django.db.models.fields.DecimalField', [], {'db_column': "'individualPreMutProteinDisoChange_origScore'", 'decimal_places': '3', 'max_digits': '8'}),
            'individualpremutproteindisochange_predictorid_fr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['disorder.Predictor']", 'db_column': "'individualPreMutProteinDisoChange_predictorID_FR'"}),
            'individualpremutproteindisochange_scorechange': ('django.db.models.fields.DecimalField', [], {'db_column': "'individualPreMutProteinDisoChange_scoreChange'", 'decimal_places': '3', 'max_digits': '8'})
        },
        'disorder.individualpreresultmutprotein': {
            'Meta': {'object_name': 'Individualpreresultmutprotein', 'db_table': "u'individualpreresultmutprotein'"},
            'individualpreresultmutprotein_end': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'individualPreResultMutProtein_end'", 'blank': 'True'}),
            'individualpreresultmutprotein_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'individualPreResultMutProtein_ID'"}),
            'individualpreresultmutprotein_mutproteinid_fr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['disorder.Mutprotein']", 'db_column': "'individualPreResultMutProtein_mutProteinID_FR'"}),
            'individualpreresultmutprotein_predictorid_fr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['disorder.Predictor']", 'db_column': "'individualPreResultMutProtein_predictorID_FR'"}),
            'individualpreresultmutprotein_sequence': ('django.db.models.fields.TextField', [], {'db_column': "'individualPreResultMutProtein_sequence'", 'blank': 'True'}),
            'individualpreresultmutprotein_start': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'individualPreResultMutProtein_start'", 'blank': 'True'})
        },
        'disorder.individualpreresultorigprotein': {
            'Meta': {'object_name': 'Individualpreresultorigprotein', 'db_table': "u'individualpreresultorigprotein'"},
            'individualpreresultorigprotein_end': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'individualPreResultOrigProtein_end'", 'blank': 'True'}),
            'individualpreresultorigprotein_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'individualPreResultOrigProtein_ID'"}),
            'individualpreresultorigprotein_predictorid_fr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['disorder.Predictor']", 'db_column': "'individualPreResultOrigProtein_predictorID_FR'"}),
            'individualpreresultorigprotein_proteinuniprot_fr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['disorder.Protein']", 'db_column': "'individualPreResultOrigProtein_proteinUniprot_FR'"}),
            'individualpreresultorigprotein_sequence': ('django.db.models.fields.TextField', [], {'db_column': "'individualPreResultOrigProtein_sequence'", 'blank': 'True'}),
            'individualpreresultorigprotein_start': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'individualPreResultOrigProtein_start'", 'blank': 'True'})
        },
        'disorder.mutprotein': {
            'Meta': {'object_name': 'Mutprotein', 'db_table': "u'mutprotein'"},
            'mutprotein_disease_id_fr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['disorder.Proteinmutationdisease']", 'db_column': "'mutProtein_disease_ID_FR'"}),
            'mutprotein_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'mutProtein_ID'"}),
            'mutprotein_mutatedaa': ('django.db.models.fields.CharField', [], {'max_length': '135', 'db_column': "'mutProtein_MutatedAA'"}),
            'mutprotein_mutationposition': ('django.db.models.fields.IntegerField', [], {'db_column': "'mutProtein_MutationPosition'"}),
            'mutprotein_orginalaa': ('django.db.models.fields.CharField', [], {'max_length': '135', 'db_column': "'mutProtein_OrginalAA'"}),
            'mutprotein_proteinuniprot_fr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['disorder.Protein']", 'db_column': "'mutProtein_ProteinUniprot_FR'"})
        },
        'disorder.predictor': {
            'Meta': {'object_name': 'Predictor', 'db_table': "u'predictor'"},
            'predictor_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'predictor_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'predictor_ID'"}),
            'predictor_name': ('django.db.models.fields.TextField', [], {}),
            'predictor_reference': ('django.db.models.fields.TextField', [], {})
        },
        'disorder.protein': {
            'Meta': {'object_name': 'Protein', 'db_table': "u'protein'"},
            'protein_description': ('django.db.models.fields.TextField', [], {}),
            'protein_length': ('django.db.models.fields.IntegerField', [], {}),
            'protein_name': ('django.db.models.fields.TextField', [], {}),
            'protein_sequence': ('django.db.models.fields.TextField', [], {}),
            'protein_uniprotaccession': ('django.db.models.fields.CharField', [], {'max_length': '135', 'primary_key': 'True', 'db_column': "'protein_uniprotAccession'"})
        },
        'disorder.proteinmutationdisease': {
            'Meta': {'object_name': 'Proteinmutationdisease', 'db_table': "u'proteinmutationdisease'"},
            'proteinmutationdisease_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'proteinMutationDisease_ID'"}),
            'proteinmutationdisease_name': ('django.db.models.fields.TextField', [], {'db_column': "'proteinMutationDisease_name'"})
        }
    }

    complete_apps = ['disorder']
