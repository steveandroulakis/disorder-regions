from django.views.generic import DetailView
from disorder_regions.disorder.models import Mutprotein, \
    Individualpreresultmutprotein, Predictor

class MutProteinDetailView(DetailView):

    model = Mutprotein
    context_object_name = "mutprotein"    #default is object_list

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        context = super(MutProteinDetailView, self).get_context_data(**kwargs)
        
        individualpreresultmutprotein_set = \
            Individualpreresultmutprotein.objects.filter( \
                individualpreresultmutprotein_mutproteinid_fr=self.object)
                
        group_by = individualpreresultmutprotein_set.values(\
        'individualpreresultmutprotein_predictorid_fr').distinct()
        
        individualpreresultmutprotein_group = []
        for value in group_by:

            predictor_id = value['individualpreresultmutprotein_predictorid_fr']
            predictor = Predictor.objects.get(predictor_id=predictor_id)
            
            individualpreresultmutprotein_by_predictor = \
                Individualpreresultmutprotein.objects.filter( \
                    individualpreresultmutprotein_mutproteinid_fr=self.object, \
                    individualpreresultmutprotein_predictorid_fr=predictor_id)

            individualpreresultmutprotein_group.append([predictor,
                individualpreresultmutprotein_by_predictor])
                    
        context['individualpreresultmutprotein_group'] = individualpreresultmutprotein_group

        return context