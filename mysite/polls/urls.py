from django.conf.urls import url

from . import views

#This is the namespace that these url are supposed to occupy
app_name = 'polls'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

# Note that the name of the matched pattern in the regexes of the second and third patterns has changed from <question_id> to <pk>.