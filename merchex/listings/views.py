from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Band,listing
from django.core.mail import send_mail
from listings.forms import ContactUsForm,BandForm,ListForm
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
    
def band_create(request):
    if request.method == 'POST':
        form=BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail',band.id) #it will return to band detail page and show the current id
    else:
        form = BandForm()
    return render(request,'listings/band_create.html',{'form': form})

def listing_create(request):
    if request.method == 'POST':
        form=ListForm(request.POST)
        if form.is_valid():
            lista = form.save()
            return redirect('listing_detail',lista.id) #it will return to band detail page and show the current id
    else:
        form = ListForm()
    return render(request,'listings/listing_create.html',{'form': form})

#update

def band_update(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # update the existing `Band` in the database
            form.save()
            # redirect to the detail page of the `Band` we just updated
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)
    form = BandForm(instance=band)
    return render(request,'listings/band_update.html',{'form': form})
    

def listing_update(request, id):
    listn = listing.objects.get(id=id)
    if request.method == 'POST':
        form = ListForm(request.POST, instance=listn)
        if form.is_valid():
            # update the existing `Band` in the database
            form.save()
            # redirect to the detail page of the `Band` we just updated
            return redirect('listing_detail', listn.id)
    else:
        form = ListForm(instance=listn)
    form = ListForm(instance=listn)
    return render(request,'listings/list_update.html',{'form': form})


def band_delete(request,id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        band.delete()

        return redirect('band_list')
    return render(request,'listings/band_delete.html',{'band':band})


def listing_delete(request,id):
    listn = listing.objects.get(id=id)

    if request.method == 'POST':
        listn.delete()

        return redirect('listing_view')
    return render(request,'listings/listing_delete.html',{'listn':listn})