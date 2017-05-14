from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^polls/latest\.html$', views.index),
    url(r'^polls/getMovie/(?P<imdb_id>[0-9]+)/$', views.get_movie),
    url(r'^polls/dialogue/(?P<imdb_id>[0-9]+)/$', views.get_dialogue),
    url(r'^polls/dialogues/(?P<imdb_id>[a-zA-Z0-9]+)/$', views.get_ajax),
    url(r'^polls/search', views.search)
]