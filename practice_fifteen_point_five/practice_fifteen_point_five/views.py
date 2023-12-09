from django.shortcuts import render
from Album.models import Album 
from Musician.models import Musician 
def home(request):
    musicians=Musician.objects.all()
    albums=Album.objects.all()
    data={
        'musicians':musicians,
        'albums':albums
    }
    return render(request,'home.html',data)

