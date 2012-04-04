from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic import DetailView

from disorder_regions.disorder.ProteinListView import ProteinListView
from disorder_regions.disorder.DiseaseListView import DiseaseListView
from disorder_regions.disorder.ProteinDetailView import ProteinDetailView
from disorder_regions.disorder.MutProteinDetailView import MutProteinDetailView

from disorder_regions.disorder.models import Protein, Disorderlab, \
    Individualpreresultorigprotein, Mutprotein, \
    Individualpreresultmutprotein

core_urls = patterns(
    'disorder_regions.disorder.views',
    (r'^$', 'index'),
    (r'^predicted/$', 'predicted'),
)

predicted_urls = patterns(
    'disorder_regions.disorder.views',
    (r'^iupred-short/1/', 'iupred_short_one'),
    (r'^iupred-short/2/', 'iupred_short_two'),
    (r'^iupred-short/3/', 'iupred_short_three'),
    (r'^iupred-short/4/', 'iupred_short_four'),
    (r'^iupred-long/1/', 'iupred_long_one'),
    (r'^iupred-long/2/', 'iupred_long_two'),
    (r'^iupred-long/3/', 'iupred_long_three'),
    (r'^iupred-long/4/', 'iupred_long_four'),
    (r'^vsl2b/1/', 'vsl2b_one'),
    (r'^vsl2b/2/', 'vsl2b_two'),
    (r'^vsl2b/3/', 'vsl2b_three'),
    (r'^vsl2b/4/', 'vsl2b_four'),         
    )

urlpatterns = patterns('',

    (r'', include(core_urls)),
    
    # Predicted urls
    (r'^predicted/', include(predicted_urls)),    
    
    (r'^disease/$',
        DiseaseListView.as_view()
    ), 

    (r'^protein/disease/(?P<disease_id>\d+)/$',
        ProteinListView.as_view()
    ),

    (r'^protein/$',
        ProteinListView.as_view()
    ), 
    
    (r'^protein/(?P<pk>\w+)/$',
        ProteinDetailView.as_view()
    ),
    
    (r'^disorderlab/(?P<pk>\w+)/$',
        DetailView.as_view(
            model=Disorderlab,
    )),    
    
    (r'^individualpreresultorigprotein/(?P<pk>\w+)/$',
        DetailView.as_view(
            model=Individualpreresultorigprotein,
    )),    
    
    (r'^mutprotein/(?P<pk>\w+)/$',
        MutProteinDetailView.as_view()
    ),
        
    (r'^individualpreresultmutprotein/(?P<pk>\w+)/$',
        DetailView.as_view(
            model=Individualpreresultmutprotein,
    )),        

    url(r'^admin/', include(admin.site.urls)),
)
