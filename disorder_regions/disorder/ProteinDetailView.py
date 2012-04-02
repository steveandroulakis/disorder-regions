from django.views.generic import DetailView
from disorder_regions.disorder.models import Protein, \
    Individualpreresultorigprotein, Predictor

class ProteinDetailView(DetailView):

    model = Protein
    context_object_name = "protein"    #default is object_list

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        context = super(ProteinDetailView, self).get_context_data(**kwargs)
        
        individualpreresultorigprotein_set = \
            Individualpreresultorigprotein.objects.filter( \
                individualpreresultorigprotein_proteinuniprot_fr=self.object)
                
        group_by = individualpreresultorigprotein_set.values(\
        'individualpreresultorigprotein_predictorid_fr').distinct()
        
        individualpreresultorigprotein_group = []
        for value in group_by:

            predictor_id = value['individualpreresultorigprotein_predictorid_fr']
            predictor = Predictor.objects.get(predictor_id=predictor_id)
            
            individualpreresultorigprotein_by_predictor = \
                Individualpreresultorigprotein.objects.filter( \
                    individualpreresultorigprotein_proteinuniprot_fr=self.object, \
                    individualpreresultorigprotein_predictorid_fr=predictor_id)

            individualpreresultorigprotein_group.append([predictor,
                individualpreresultorigprotein_by_predictor])
                    
        context['individualpreresultorigprotein_group'] = individualpreresultorigprotein_group

        return context