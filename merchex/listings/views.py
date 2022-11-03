from django.shortcuts import render
from django.http import HttpResponse
from .models import Band,listing
# Create your views here.

def hello(request):
    bands = Band.objects.all()
    return render(request,'listings/hello.html',{'bands':bands})

def listing_view(request):
    lista = listing.objects.all()
    context = {
        'listn':lista
    }
    return render(request,'listings/listing.html',context)

def about(request):
    return HttpResponse('<h1>Welcome to our About Page!</h1>')

def contact(request):
     return HttpResponse('<h1>Welcome to our Contact-Us Page!</h1>')