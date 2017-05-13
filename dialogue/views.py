from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from django.template import loader
# Create your views here.

def detail(request, question_id):
    q = Movie.objects.get(pk = question_id)
    return HttpResponse(q.title)

def index(request):
    latest_question_list = Movie.objects.all()
    template = loader.get_template('dialogue/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def get_movie(request , imdb_id):
    template = loader.get_template('dialogue/movie.html')
    try:
        m = Movie.objects.all().filter(imdb_id = str(imdb_id))
        context = {
            'latest_question_list': m,
        }
        return HttpResponse(template.render(context, request))
    except:
        return HttpResponse('<h1>Not Found Hah</h1>')