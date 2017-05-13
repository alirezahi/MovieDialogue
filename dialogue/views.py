from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from django.template import loader
import json
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

def get_dialogue(request , imdb_id):
    template = loader.get_template('dialogue/dialogue.html')
    try:
        m = Movie.objects.all().filter(imdb_id = str(imdb_id))
        context = {
            'latest_question_list': m,
        }
        return HttpResponse(template.render(context, request))
    except:
        return HttpResponse('<h1>Not Found Hah</h1>')



def get_ajax(request , imdb_id):


    some_data_to_dump = {
        'some_var_1': 'foo',
        'some_var_2': 'bar',
    }

    data = json.dumps(some_data_to_dump)
    return HttpResponse(data,content_type='application/json')

def search(request):
    template = loader.get_template('dialogue/Search.html')
    return HttpResponse(template.render())