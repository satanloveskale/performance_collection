# from django.conf.urls import url
# from . import views

# urlpatterns = [
    # url(r'^$', views.score_list, name='score_list'),
   
# ]
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from django.conf.urls import include
from performance_collection.views import (
    score_listview,
    ScoreListView,
    ScoreDetailView,
    OrchestralListView,
    ChoralListView,
    BandListView,
    ScoreSearchView,

)



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^search/?', include('haystack.urls')),
    url(r'^performance_collection/$', ScoreListView.as_view()),
    url(r'^performance_collection/orchestral/$', OrchestralListView.as_view()),
    url(r'^performance_collection/choral/$', ChoralListView.as_view()),
    url(r'^performance_collection/band/$', BandListView.as_view()),
    url(r'^performance_collection/(?P<slug>[\w-]+)/$', ScoreDetailView.as_view()),

]

