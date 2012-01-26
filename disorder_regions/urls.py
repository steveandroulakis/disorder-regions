from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic import DetailView

from disorder_regions.disorder.ProteinListView import ProteinListView
from disorder_regions.disorder.models import Protein

core_urls = patterns(
    'disorder_regions.disorder.views',
    (r'^$', 'index'),
)

urlpatterns = patterns('',

    (r'', include(core_urls)),

    (r'^protein/$',
        ProteinListView.as_view()
    ),
    
    (r'^protein/(?P<pk>\w+)/$',
        DetailView.as_view(
            model=Protein,
    )),    

    url(r'^admin/', include(admin.site.urls)),
)
