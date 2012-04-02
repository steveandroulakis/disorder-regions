from django.views.generic import ListView
from disorder_regions.disorder.models import Protein,\
    Proteinmutationdisease

class ProteinListView(ListView):

    model = Protein
    context_object_name = "protein_list"    #default is object_list
    paginate_by = 2500
    
    def get_context_data(self, **kwargs):

        context = super(ProteinListView, self).get_context_data(**kwargs)

        protein_list = Protein.objects.all()
            
        if 'disease_id' in self.kwargs:
            disease_id = self.kwargs['disease_id']
            context['disease'] = Proteinmutationdisease.objects.get(proteinmutationdisease_id=disease_id)
            
            protein_list = protein_list.filter(mutprotein__mutprotein_disease_id_fr=disease_id).distinct()
            
        context['protein_list'] = protein_list
        
        return context    