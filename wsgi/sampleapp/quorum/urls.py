
from django.conf.urls import patterns,url
urlpatterns = patterns('quorum.views',
    url(r'^$', 'home'),
    url(r'^question/add/$', 'add_question'),
    url(r'^topic/(\d+)/$', 'questions'),
    url(r'^question/all/$','questions'),
    url(r'^question/(\d+)/$', 'question'),
    url(r'^question/markfav/$', 'mark_as_favorite'),
    url(r'^topic/follow/$', 'mark_follow'),
    url(r'^user/(?P<username>\w+)/$', 'quorumuser'),  
    url (r'^users/$', 'quorumusers'),
    url (r'^contactinfo/save/$', 'save_contact_info'),
)
