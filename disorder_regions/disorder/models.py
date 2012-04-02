from django.db import models
from disorder_regions.disorder.shortcuts import highlight_region, \
    highlight_mutation

class Protein(models.Model):
    protein_uniprotaccession = models.CharField(max_length=135, primary_key=True, db_column='protein_uniprotAccession')
    protein_name = models.TextField()
    protein_length = models.IntegerField()
    protein_description = models.TextField()
    protein_sequence = models.TextField()
    class Meta:
        db_table = u'protein'
        
    def __unicode__(self):
        return str(self.protein_name)
        
class Disorderlab(models.Model):
    disorderlab_id = models.IntegerField(primary_key=True, db_column='disorderLab_ID')
    disorderlab_proteinuniprot_fr = models.ForeignKey(Protein, db_column='disorderLab_proteinUniprot_FR')
    disorderlab_disprotacession = models.CharField(max_length=45, db_column='disorderLab_disprotAccession')
    class Meta:
        db_table = u'disorderlab'
    def __unicode__(self):
        return str(self.disorderlab_id)
    def disorderlab_disprotacession_nullcheck(self):
        if self.disorderlab_disprotacession == None \
            or 'null':
            return 'None'
        else:
            return self.disorderlab_disprotacession
        # return highlight_region(
        #     self.disorderlab_proteinuniprot_fr.protein_sequence,
        #     self.disorderlab_start,
        #     self.disorderlab_end)             

class Disorderpredictorresults(models.Model):
    disorderpredictorresult_id = models.IntegerField(primary_key=True, db_column='disorderPredictorResult_ID')
    disorderpredictorresult_proteinid_fr = models.IntegerField(db_column='disorderPredictorResult_proteinID_FR')
    disorderpredictorresult_start = models.IntegerField(db_column='disorderPredictorResult_start')
    disorderpredictorresult_end = models.IntegerField(db_column='disorderPredictorResult_end')
    disorderpredictorresult_sequence = models.TextField(db_column='disorderPredictorResult_sequence')
    class Meta:
        db_table = u'disorderpredictorresults'
        
class Predictor(models.Model):
    predictor_id = models.IntegerField(primary_key=True, db_column='predictor_ID')
    predictor_name = models.TextField()
    predictor_description = models.TextField(blank=True)
    predictor_reference = models.TextField()
    class Meta:
        db_table = u'predictor'   
        
class Proteinmutationdisease(models.Model):
    proteinmutationdisease_id = models.IntegerField(primary_key=True, db_column='proteinMutationDisease_ID')
    proteinmutationdisease_name = models.TextField(db_column='proteinMutationDisease_name')
    class Meta:
        db_table = u'proteinmutationdisease'        
        
class Mutprotein(models.Model):
    mutprotein_id = models.IntegerField(primary_key=True, db_column='mutProtein_ID')
    mutprotein_proteinuniprot_fr = models.ForeignKey(Protein, db_column='mutProtein_ProteinUniprot_FR')
    mutprotein_orginalaa = models.CharField(max_length=135, db_column='mutProtein_OrginalAA')
    mutprotein_mutationposition = models.IntegerField(db_column='mutProtein_MutationPosition')
    mutprotein_mutatedaa = models.CharField(max_length=135, db_column='mutProtein_MutatedAA')
    mutprotein_disease_id_fr = models.ForeignKey(Proteinmutationdisease, db_column='mutProtein_disease_ID_FR')
    class Meta:
        db_table = u'mutprotein' 
        
    def __unicode__(self):
        return highlight_mutation(
            self.mutprotein_proteinuniprot_fr.protein_sequence,
            self.mutprotein_mutationposition,
            self.mutprotein_mutatedaa)                    

class Individualpremutproteindisochange(models.Model):
    individualpremutproteindisochange_id = models.IntegerField(primary_key=True, db_column='individualPreMutProteinDisoChange_ID')
    individualpremutproteindisochange_predictorid_fr = models.ForeignKey(Predictor, db_column='individualPreMutProteinDisoChange_predictorID_FR')
    individualpremutproteindisochange_mutproteinid_fr = models.ForeignKey(Mutprotein, db_column='individualPreMutProteinDisoChange_mutProteinID_FR')
    individualpremutproteindisochange_mutposition = models.IntegerField(db_column='individualPreMutProteinDisoChange_mutPosition')
    individualpremutproteindisochange_origaa = models.CharField(max_length=135, db_column='individualPreMutProteinDisoChange_origAA')
    individualpremutproteindisochange_origscore = models.DecimalField(decimal_places=3, max_digits=8, db_column='individualPreMutProteinDisoChange_origScore')
    individualpremutproteindisochange_mutaa = models.CharField(max_length=135, db_column='individualPreMutProteinDisoChange_mutAA')
    individualpremutproteindisochange_mutscore = models.DecimalField(decimal_places=3, max_digits=8, db_column='individualPreMutProteinDisoChange_mutScore')
    individualpremutproteindisochange_scorechange = models.DecimalField(decimal_places=3, max_digits=8, db_column='individualPreMutProteinDisoChange_scoreChange')
    individualpremutproteindisochange_disorderchange = models.CharField(max_length=135, db_column='individualPreMutProteinDisoChange_disorderChange')
    class Meta:
        db_table = u'individualpremutproteindisochange'

class Individualpreresultmutprotein(models.Model):
    individualpreresultmutprotein_id = models.IntegerField(primary_key=True, db_column='individualPreResultMutProtein_ID')
    individualpreresultmutprotein_mutproteinid_fr = models.ForeignKey(Mutprotein, db_column='individualPreResultMutProtein_mutProteinID_FR')
    individualpreresultmutprotein_predictorid_fr = models.ForeignKey(Predictor, db_column='individualPreResultMutProtein_predictorID_FR')
    individualpreresultmutprotein_start = models.IntegerField(null=True, db_column='individualPreResultMutProtein_start', blank=True)
    individualpreresultmutprotein_end = models.IntegerField(null=True, db_column='individualPreResultMutProtein_end', blank=True)
    individualpreresultmutprotein_sequence = models.TextField(db_column='individualPreResultMutProtein_sequence', blank=True)
    class Meta:
        db_table = u'individualpreresultmutprotein'
        
    def __unicode__(self):
        return highlight_region(
            self.individualpreresultmutprotein_mutproteinid_fr.mutprotein_proteinuniprot_fr.protein_sequence,
            self.individualpreresultmutprotein_start,
            self.individualpreresultmutprotein_end)        

class Individualpreresultorigprotein(models.Model):
    individualpreresultorigprotein_id = models.IntegerField(primary_key=True, db_column='individualPreResultOrigProtein_ID')
    individualpreresultorigprotein_proteinuniprot_fr = models.ForeignKey(Protein, db_column='individualPreResultOrigProtein_proteinUniprot_FR')
    individualpreresultorigprotein_predictorid_fr = models.ForeignKey(Predictor, db_column='individualPreResultOrigProtein_predictorID_FR')
    individualpreresultorigprotein_start = models.IntegerField(null=True, db_column='individualPreResultOrigProtein_start', blank=True)
    individualpreresultorigprotein_end = models.IntegerField(null=True, db_column='individualPreResultOrigProtein_end', blank=True)
    individualpreresultorigprotein_sequence = models.TextField(db_column='individualPreResultOrigProtein_sequence', blank=True)
    class Meta:
        db_table = u'individualpreresultorigprotein'
        
    def __unicode__(self):
        return highlight_region(
            self.individualpreresultorigprotein_proteinuniprot_fr.protein_sequence,
            self.individualpreresultorigprotein_start,
            self.individualpreresultorigprotein_end)