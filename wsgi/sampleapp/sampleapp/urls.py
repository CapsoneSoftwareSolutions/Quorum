from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sampleapp.views.home', name='home'),
    # url(r'^sampleapp/', include('sampleapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'quorum.views.home', name='home'),
url(r'^quorum/', include('quorum.urls')),
url(r'^accounts/', include('registration.urls')),
url(r'^users/(?P<username>\w+)/$', 'quorum.views.quorumuser'), 
url(r'^search/', include('haystack.urls')),
url(r'^tasks/$', 'quorum.views.tasks'), 
#url(r'^txtarea/$', 'quorum.views.txtarea'), 
url (r'^privacypolicy/$', 'quorum.views.privacypolicy'),
url (r'^help/$', 'quorum.views.help'),

url (r'^feedback/$', 'quorum.views.feedbacks'),
)

from haystack.query import SearchQuerySet
sqs = SearchQuerySet()#.filter(topic='Gaming')
from haystack.views import SearchView, search_view_factory
#from quorum.forms import DateRangeSearchForm
urlpatterns += patterns('haystack.views',
    url(r'^quorum/search/$', search_view_factory(
        view_class=SearchView,
        template='quorum/search.html',
        searchqueryset=sqs,
        #form_class=DateRangeSearchForm
    ), name='haystack_search'),
)