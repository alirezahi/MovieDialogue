from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^polls/latest\.html$', views.index)
]