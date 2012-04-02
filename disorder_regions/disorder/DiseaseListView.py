from django.views.generic import ListView
from disorder_regions.disorder.models import Proteinmutationdisease
from django.db.models import Count

class DiseaseListView(ListView):

    proteinmutationdisease_distinct = \
        Proteinmutationdisease.objects.annotate(num_proteins=Count('mutprotein__mutprotein_proteinuniprot_fr__protein_uniprotaccession', distinct=True))
    
    proteinmutationdisease_distinct = proteinmutationdisease_distinct.\
        order_by('-num_proteins')

    queryset = proteinmutationdisease_distinct
    context_object_name = "proteinmutationdisease_list"    #default is object_list
    paginate_by = 3000