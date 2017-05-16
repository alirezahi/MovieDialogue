from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie,Genre,Country,Series,Actor,Dialogue
from django.template import loader
import json , requests
import datetime
# Create your views here.

def detail(request, question_id):
    q = Movie.objects.get(pk = question_id)
    return HttpResponse(q.title)

def index(request):
    latest_question_list = Movie.objects.all()
    latest_series_list = Series.objects.all()
    template = loader.get_template('dialogue/index.html')
    context = {
        'latest_question_list': latest_question_list,
        'series_list' : latest_series_list,
    }
    return HttpResponse(template.render(context, request))

def get_movie(request , imdb_id):
    template = loader.get_template('dialogue/movie.html')
    try:
        m = Movie.objects.all().filter(imdb_id = str(imdb_id))
        context = {
            'movies': m,
        }
        return HttpResponse(template.render(context, request))
    except:
        return HttpResponse('<h1>Not Found Hah</h1>')

def get_series(request , imdb_id):
    template = loader.get_template('dialogue/series.html')
    try:
        m = Series.objects.all().filter(imdb_id = str(imdb_id))
        context = {
            'series': m,
        }
        return HttpResponse(template.render(context, request))
    except:
        return HttpResponse('<h1>Not Found Hah</h1>')

def get_actor(request, actor_name):
    actor_name = actor_name.replace('20',' ')
    template = loader.get_template('dialogue/actor.html')
    try:
        actor_obj = Actor.objects.all().filter(name=actor_name)
        m = Movie.objects.all().filter(actors=actor_obj)
        s = Series.objects.all().filter(actors=actor_obj)
        context = {
            'movie_actor': m,
            'series_actor' : s,
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
    url = 'http://www.omdbapi.com/?'

    params = dict(
        i=imdb_id
    )
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    try:
        if data['Type'] == 'movie':
            m = Movie.objects.get(imdb_id = imdb_id)
            some_data_to_dump = {
                'movie_name': m.title,
                'status': 'failed',
            }
        else:
            m = Series.objects.get(imdb_id=imdb_id)
            some_data_to_dump = {
                'movie_name': m.title,
                'status': 'failed',
            }
    except:
        if data['Type'] == 'movie':
            m = Movie(imdb_id=imdb_id,title=data['Title'],year=data['Year'],image=data['Poster'],plot=data['Plot'],runtime=data['Runtime'])
            m.save()
            for genre_name in data['Genre'].split(','):

                try:
                    a = Genre.objects.get(name=genre_name.strip())
                except:
                    a = Genre(name=genre_name.strip())
                    a.save()
                m.genre.add(a)
            for actor_name in data['Actors'].split(','):
                try:
                    a = Actor.objects.get(name=actor_name.strip())
                except:
                    a = Actor(name=actor_name.strip(),link=str(actor_name.strip().replace(' ','20')))
                    a.save()
                m.actors.add(a)
            for country_name in data['Country'].split(','):
                try:
                    a = Country.objects.get(name=country_name.strip())
                except:
                    a = Country(name=country_name.strip())
                    a.save()
                m.country.add(a)
            some_data_to_dump = {
                'movie_name': m.title,
                'status': 'ok',
            }
        else:
            m = Series(imdb_id=imdb_id, title=data['Title'], year=data['Year'], image=data['Poster'], plot=data['Plot'],runtime=data['Runtime'],seasons=data['totalSeasons'])
            m.save()
            for genre_name in data['Genre'].split(','):

                try:
                    a = Genre.objects.get(name=genre_name.strip())
                except:
                    a = Genre(name=genre_name.strip())
                    a.save()
                m.genre.add(a)
            for actor_name in data['Actors'].split(','):
                try:
                    a = Actor.objects.get(name=actor_name.strip())
                except:
                    a = Actor(name=actor_name.strip(), link=str(actor_name.strip().replace(' ', '20')))
                    a.save()
                m.actors.add(a)
            for country_name in data['Country'].split(','):
                try:
                    a = Country.objects.get(name=country_name.strip())
                except:
                    a = Country(name=country_name.strip())
                    a.save()
                m.country.add(a)
            some_data_to_dump = {
                'movie_name': m.title,
                'status': 'ok',
            }
    data = json.dumps(some_data_to_dump)
    return HttpResponse(data,content_type='application/json')

def search(request):
    template = loader.get_template('dialogue/Search.html')
    return HttpResponse(template.render())

def get_get(request):
    p = request.GET['p']
    imdb_id = request.GET['imdb_id']
    m = Movie.objects.get(imdb_id=imdb_id)
    d = Dialogue(content=p,pub_date=datetime.datetime.now(),movie=m)
    d.save()
    return HttpResponse()