from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(R'^$', 'apps.homepage.views.index' ),
)
