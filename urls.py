from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^wikistudies/', include('wikistudies.foo.urls')),
    (r'^studies/$', 'study.views.studyIndex'),
    (r'^studies/(?P<study_id>\d+)/$', 'study.views.studyDetail'),
    #(r'^authors/$', 'study.views.authorIndex'),
    #(r'^authors/(?P<author_id>\d+)/$', 'study.views.authorDetail'),
    #(r'^users/$', 'study.views.userIndex'),
    #(r'^users/(?P<user_id>\d+)/$', 'study.views.userDetail'),
    

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls))
)
