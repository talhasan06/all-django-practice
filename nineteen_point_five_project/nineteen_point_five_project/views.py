from django.shortcuts import render
from first_app.models import Musician
def home(request):
    data = Musician.objects.all()
    return render (request,'home.html',{'data':data})
