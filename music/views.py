from django.shortcuts import render,get_object_or_404
#from django.http import HttpResponse
from .models import Album
#from django.http import Http404
#from django.template import loader


# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    #html = ""
    #for album in all_albums:
    #    url = '/music/' + str(album.id) + '/'
    #    html += "<a href='" + url + "'>" + album.album_title + "</a><br>"
    #return HttpResponse(html)

    #template = loader.get_template("music/index.html")

    context = {
        "all_albums" : all_albums,
    }
    #return HttpResponse(template.render(context, request))

    return render(request, "music/index.html", context)


def detail(request, album_id):
    #return HttpResponse("<h1>Details for Album id:"+str(album_id)+"<h1>")

    #try:
    #    album = Album.objects.get(pk=album_id)
    #except Album.DoesNotExist:
    #    raise Http404("Album does not exist")

    album = get_object_or_404(Album, pk=album_id)
    return render(request, "music/detail.html", {"album":album})
