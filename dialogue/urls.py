from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^polls/latest\.html$', views.index),
    url(r'^polls/getMovie/(?P<imdb_id>[a-zA-Z0-9]+)/$', views.get_movie),
    url(r'^polls/getGet/$', views.get_get),
    url(r'^polls/getSeries/(?P<imdb_id>[a-zA-Z0-9]+)/$', views.get_series),
    url(r'^polls/dialogue/(?P<imdb_id>[a-zA-Z0-9]+)/$', views.get_dialogue),
    url(r'^polls/actor/(?P<actor_name>[a-zA-Z0-9]+)/$', views.get_actor),
    url(r'^polls/dialogues/(?P<imdb_id>[a-zA-Z0-9]+)/$', views.get_ajax),
    url(r'^polls/search', views.search)
]