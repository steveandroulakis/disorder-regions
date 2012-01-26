from django.views.generic import ListView
from disorder_regions.disorder.models import Protein

class ProteinListView(ListView):

    model = Protein
    context_object_name = "protein_list"    #default is object_list
    paginate_by = 20
