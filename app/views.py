from django.shortcuts import render
from .models import Musician
from .models import Album
def index(request):
    qr=Album.objects.filter()
    return render(request,"index.html",{"qr":qr})