from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Band,listing
from django.core.mail import send_mail
from listings.forms import ContactUsForm
# Create your views here.

def band_list(request):
    bands = Band.objects.all()
    return render(request,'listings/band_list.html',{'bands':bands})

def band_detail(request,id):
    band = Band.objects.get(id=id)
    return render(request,'listings/band_detail.html',{'band':band})

def listing_view(request):
    lista = listing.objects.all()
    context = {
        'listn':lista
    }
    return render(request,'listings/listing.html',context)

def listing_detail(request,id):
    lista = listing.objects.get(pk=id)
    return render(request,'listings/listing_detail.html',{'lista':lista})

def about(request):
    return HttpResponse('<h1>Welcome to our About Page!</h1>')

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
   # print('The request method is: ',request.method)
    #print('The POST data is: ',request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonymous"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
        )
        return redirect('email-sent') #usually to log in page
    else:
        # this must be a GET request, so create an empty form
        form = ContactUsForm()
    return render(request,'listings/contact.html',{'form':form})
    