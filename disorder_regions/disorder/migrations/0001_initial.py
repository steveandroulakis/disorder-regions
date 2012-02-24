# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Protein'
        db.create_table(u'protein', (
            ('protein_uniprotaccession', self.gf('django.db.models.fields.CharField')(max_length=135, primary_key=True, db_column='protein_uniprotAccession')),
            ('protein_name', self.gf('django.db.models.fields.TextField')()),
            ('protein_length', self.gf('django.db.models.fields.IntegerField')()),
            ('protein_description', self.gf('django.db.models.fields.TextField')()),
            ('protein_sequence', self.gf('django.db.models.fields.TextField')()),
            ('protein_percentageofdisorder', self.gf('django.db.models.fields.DecimalField')(db_column='protein_percentageOfDisorder', decimal_places=3, max_digits=7)),
        ))
        db.send_create_signal('disorder', ['Protein'])

        # Adding model 'Disorderlabfunction'
        db.create_table(u'disorderlabfunction', (
            ('disorderlabfunction_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='disorderLabFunction_ID')),
            ('disorderlabfunction_name', self.gf('django.db.models.fields.TextField')(db_column='disorderLabFunction_name')),
        ))
        db.send_create_signal('disorder', ['Disorderlabfunction'])

        # Adding model 'Disorderlabmethod'
        db.create_table(u'disorderlabmethod', (
            ('disorderlabmethod_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='disorderLabMethod_ID')),
            ('disorderlabmethod_name', self.gf('django.db.models.fields.TextField')(db_column='disorderLabMethod_name')),
            ('disorderlabmethod_description', self.gf('django.db.models.fields.TextField')(db_column='disorderLabMethod_description', blank=True)),
            ('disorderlabmethod_reference', self.gf('django.db.models.fields.TextField')(db_column='disorderLabMethod_reference', blank=True)),
        ))
        db.send_create_signal('disorder', ['Disorderlabmethod'])

        # Adding model 'Disorderlab'
        db.create_table(u'disorderlab', (
            ('disorderlab_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='disorderLab_ID')),
            ('disorderlab_proteinuniprot_fr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['disorder.Protein'], db_column='disorderLab_proteinUniprot_FR')),
            ('disorderlab_start', self.gf('django.db.models.fields.IntegerField')(db_column='disorderLab_start')),
            ('disorderlab_end', self.gf('django.db.models.fields.IntegerField')(db_column='disorderLab_end')),
            ('disorderlab_sequence', self.gf('django.db.models.fields.TextField')(db_column='disorderLab_sequence')),
            ('disorderlab_functionid_fr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['disorder.Disorderlabfunction'], db_column='disorderLab_functionID_FR')),
            ('disorderlab_methodid_fr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['disorder.Disorderlabmethod'], db_column='disorderLab_methodID_FR')),
        ))
        db.send_create_signal('disorder', ['Disorderlab'])

        # Adding model 'Disorderpredictorresults'
        db.create_table(u'disorderpredictorresults', (
            ('disorderpredictorresult_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='disorderPredictorResult_ID')),
            ('disorderpredictorresult_proteinid_fr', self.gf('django.db.models.fields.IntegerField')(db_column='disorderPredictorResult_proteinID_FR')),
            ('disorderpredictorresult_start', self.gf('django.db.models.fields.IntegerField')(db_column='disorderPredictorResult_start')),
            ('disorderpredictorresult_end', self.gf('django.db.models.fields.IntegerField')(db_column='disorderPredictorResult_end')),
            ('disorderpredictorresult_sequence', self.gf('django.db.models.fields.TextField')(db_column='disorderPredictorResult_sequence')),
        ))
        db.send_create_signal('disorder', ['Disorderpredictorresults'])

        # Adding model 'Predictor'
        db.create_table(u'predictor', (
            ('predictor_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='predictor_ID')),
            ('predictor_name', self.gf('django.db.models.fields.TextField')()),
            ('predictor_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('predictor_reference', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('disorder', ['Predictor'])

        # Adding model 'Proteinmutationdisease'
        db.create_table(u'proteinmutationdisease', (
            ('proteinmutationdisease_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='proteinMutationDisease_ID')),
            ('proteinmutationdisease_name', self.gf('django.db.models.fields.TextField')(db_column='proteinMutationDisease_name')),
            ('proteinmutationdisease_description', self.gf('django.db.models.fields.TextField')(db_column='proteinMutationDisease_description', blank=True)),
        ))
        db.send_create_signal('disorder', ['Proteinmutationdisease'])

        # Adding model 'Mutprotein'
        db.create_table(u'mutprotein', (
            ('mutprotein_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='mutProtein_ID')),
            ('mutprotein_proteinuniprot_fr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['disorder.Protein'], db_column='mutProtein_ProteinUniprot_FR')),
            ('mutprotein_orginalaa', self.gf('django.db.models.fields.CharField')(max_length=135, db_column='mutProtein_OrginalAA')),
            ('mutprotein_mutationposition', self.gf('django.db.models.fields.IntegerField')(db_column='mutProtein_MutationPosition')),
            ('mutprotein_mutatedaa', self.gf('django.db.models.fields.CharField')(max_length=135, db_column='mutProtein_MutatedAA')),
            ('mutprotein_disease_id_fr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['disorder.Proteinmutationdisease'], db_column='mutProtein_disease_ID_FR')),
        ))
        db.send_create_signal('disorder', ['Mutprotein'])

        # Adding model 'Individualpremutproteindisochange'
        db.create_table(u'individualpremutproteindisochange', (
            ('individualpremutproteindisochange_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='individualPreMutProteinDisoChange_ID')),
            ('individualpremutproteindisochange_predictorid_fr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['disorder.Predictor'], db_column='individualPreMutProteinDisoChange_predictorID_FR')),
            ('individualpremutproteindisochange_mutproteinid_fr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['disorder.Mutprotein'], db_column='individualPreMutProteinDisoChange_mutProteinID_FR')),
            ('individualpremutproteindisochange_mutposition', self.gf('django.db.models.fields.IntegerField')(db_column='individualPreMutProteinDisoChange_mutPosition')),
            ('individualpremutproteindisochange_origaa', self.gf('django.db.models.fields.CharField')(max_length=135, db_column='individualPreMutProteinDisoChange_origAA')),
            ('individualpremutproteindisochange_origscore', self.gf('django.db.models.fields.DecimalField')(db_column='individualPreMutProteinDisoChange_origScore', decimal_places=3, max_digits=8)),
            ('individualpremutproteindisochange_mutaa', self.gf('django.db.models.fields.CharField')(max_length=135, db_column='individualPreMutProteinDisoChange_mutAA')),
            ('individualpremutproteindisochange_mutscore', self.gf('django.db.models.fields.DecimalField')(db_column='individualPreMutProteinDisoChange_mutScore', decimal_places=3, max_digits=8)),
            ('individualpremutproteindisochange_scorechange', self.gf('django.db.models.fields.DecimalField')(db_column='individualPreMutProteinDisoChange_scoreChange', decimal_places=3, max_digits=8)),
            ('individualpremutproteindisochange_disorderchange', self.gf('django.db.models.fields.CharField')(max_length=135, db_column='individualPreMutProteinDisoChange_disorderChange')),
        ))
        db.send_create_signal('disorder', ['Individualpremutproteindisochange'])

        # Adding model 'Individualpreresultmutprotein'
        db.create_table(u'individualpreresultmutprotein', (
            ('individualpreresultmutprotein_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='individualPreResultMutProtein_ID')),
            ('individualpreresultmutprotein_mutproteinid_fr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['disorder.Mutprotein'], db_column='individualPreResultMutProtein_mutProteinID_FR')),
            ('individualpreresultmutprotein_predictorid_fr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['disorder.Predictor'], db_column='individualPreResultMutProtein_predictorID_FR')),
            ('individualpreresultmutprotein_uniprot_fr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['disorder.Protein'], db_column='individualPreResultMutProtein_Uniprot_FR')),
            ('individualpreresultmutprotein_start', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='individualPreResultMutProtein_start', blank=True)),
            ('individualpreresultmutprotein_end', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='individualPreResultMutProtein_end', blank=True)),
            ('individualpreresultmutprotein_sequence', self.gf('django.db.models.fields.TextField')(db_column='individualPreResultMutProtein_sequence', blank=True)),
        ))
        db.send_create_signal('disorder', ['Individualpreresultmutprotein'])

        # Adding model 'Individualpreresultorigprotein'
        db.create_table(u'individualpreresultorigprotein', (
            ('individualpreresultorigprotein_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='individualPreResultOrigProtein_ID')),
            ('individualpreresultorigprotein_proteinuniprot_fr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['disorder.Protein'], db_column='individualPreResultOrigProtein_proteinUniprot_FR')),
            ('individualpreresultorigprotein_predictorid_fr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['disorder.Predictor'], db_column='individualPreResultOrigProtein_predictorID_FR')),
            ('individualpreresultorigprotein_start', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='individualPreResultOrigProtein_start', blank=True)),
            ('individualpreresultorigprotein_end', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='individualPreResultOrigProtein_end', blank=True)),
            ('individualpreresultorigprotein_sequence', self.gf('django.db.models.fields.TextField')(db_column='individualPreResultOrigProtein_sequence', blank=True)),
        ))
        db.send_create_signal('disorder', ['Individualpreresultorigprotein'])


    def backwards(self, orm):
        
        # Deleting model 'Protein'
        db.delete_table(u'protein')

        # Deleting model 'Disorderlabfunction'
        db.delete_table(u'disorderlabfunction')

        # Deleting model 'Disorderlabmethod'
        db.delete_table(u'disorderlabmethod')

        # Deleting model 'Disorderlab'
        db.delete_table(u'disorderlab')

        # Deleting model 'Disorderpredictorresults'
        db.delete_table(u'disorderpredictorresults')

        # Deleting model 'Predictor'
        db.delete_table(u'predictor')

        # Deleting model 'Proteinmutationdisease'
        db.delete_table(u'proteinmutationdisease')

        # Deleting model 'Mutprotein'
        db.delete_table(u'mutprotein')

        # Deleting model 'Individualpremutproteindisochange'
        db.delete_table(u'individualpremutproteindisochange')

        # Deleting model 'Individualpreresultmutprotein'
        db.delete_table(u'individualpreresultmutprotein')

        # Deleting model 'Individualpreresultorigprotein'
        db.delete_table(u'individualpreresultorigprotein')


    models = {
        'disorder.disorderlab': {
            'Meta': {'object_name': 'Disorderlab', 'db_table': "u'disorderlab'"},
            'disorderlab_end': ('django.db.models.fields.IntegerField', [], {'db_column': "'disorderLab_end'"}),
            'disorderlab_functionid_fr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['disorder.Disorderlabfunction']", 'db_column': "'disorderLab_functionID_FR'"}),
            'disorderlab_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'disorderLab_ID'"}),
            'disorderlab_methodid_fr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['disorder.Disorderlabmethod']", 'db_column': "'disorderLab_methodID_FR'"}),
            'disorderlab_proteinuniprot_fr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['disorder.Protein']", 'db_column': "'disorderLab_proteinUniprot_FR'"}),
            'disorderlab_sequence': ('django.db.models.fields.TextField', [], {'db_column': "'disorderLab_sequence'"}),
            'disorderlab_start': ('django.db.models.fields.IntegerField', [], {'db_column': "'disorderLab_start'"})
        },
        'disorder.disorderlabfunction': {
            'Meta': {'object_name': 'Disorderlabfunction', 'db_table': "u'disorderlabfunction'"},
            'disorderlabfunction_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'disorderLabFunction_ID'"}),
            'disorderlabfunction_name': ('django.db.models.fields.TextField', [], {'db_column': "'disorderLabFunction_name'"})
        },
        'disorder.disorderlabmethod': {
            'Meta': {'object_name': 'Disorderlabmethod', 'db_table': "u'disorderlabmethod'"},
            'disorderlabmethod_description': ('django.db.models.fields.TextField', [], {'db_column': "'disorderLabMethod_description'", 'blank': 'True'}),
            'disorderlabmethod_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'disorderLabMethod_ID'"}),
            'disorderlabmethod_name': ('django.db.models.fields.TextField', [], {'db_column': "'disorderLabMethod_name'"}),
            'disorderlabmethod_reference': ('django.db.models.fields.TextField', [], {'db_column': "'disorderLabMethod_reference'", 'blank': 'True'})
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
            'individualpreresultmutprotein_start': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'individualPreResultMutProtein_start'", 'blank': 'True'}),
            'individualpreresultmutprotein_uniprot_fr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['disorder.Protein']", 'db_column': "'individualPreResultMutProtein_Uniprot_FR'"})
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
            'protein_percentageofdisorder': ('django.db.models.fields.DecimalField', [], {'db_column': "'protein_percentageOfDisorder'", 'decimal_places': '3', 'max_digits': '7'}),
            'protein_sequence': ('django.db.models.fields.TextField', [], {}),
            'protein_uniprotaccession': ('django.db.models.fields.CharField', [], {'max_length': '135', 'primary_key': 'True', 'db_column': "'protein_uniprotAccession'"})
        },
        'disorder.proteinmutationdisease': {
            'Meta': {'object_name': 'Proteinmutationdisease', 'db_table': "u'proteinmutationdisease'"},
            'proteinmutationdisease_description': ('django.db.models.fields.TextField', [], {'db_column': "'proteinMutationDisease_description'", 'blank': 'True'}),
            'proteinmutationdisease_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'proteinMutationDisease_ID'"}),
            'proteinmutationdisease_name': ('django.db.models.fields.TextField', [], {'db_column': "'proteinMutationDisease_name'"})
        }
    }

    complete_apps = ['disorder']
