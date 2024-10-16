from django.shortcuts import render
from .models import Actor, Movie
from django.http import HttpResponse

def add_movie(request):
    if request.method == "POST":
        title = request.POST['title']
        director = request.POST['director']
        release_date = request.POST['release_date']
        genre = request.POST['genre']
        lead_actor_id = request.POST['lead_actor']

        lead_actor = Actor.objects.get(id=lead_actor_id)

        movie = Movie(
            title=title,
            director=director,
            release_date=release_date,
            genre=genre,
            lead_actor=lead_actor
        )
        movie.save()
        return HttpResponse(f"Movie '{movie.title}' added successfully")

    actors = Actor.objects.all();
    return render(request, 'index.html', {'actors': actors})