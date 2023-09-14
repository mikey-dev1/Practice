from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from users.forms import *
from users.models import *
from .forms import *
from .filters import ListingFilter

def landing_view(request):
 return render(request, "views/main.html", {"name": "big Mike"})

def new_page(request):
 return HttpResponse(request, '<h1> this is new page</h1>')

@login_required
def home_view(request):
  listings = listing.objects.all()
  listing_filter = ListingFilter(request.GET, queryset=listings)
  context = {
    'listing_filter': listing_filter
  }
  return render(request, 'views/home.html', context)


@login_required
def list_view(request):
 if request.method == 'POST':
  try:
   listing_form = ListingForm(request.POST, request.FILES)
   location_form = LocationForm(request.POST)
   if listing_form.is_valid() and location_form.is_valid():
    listing = listing_form.save(commit=False)
    listing_location = location_form.save()
    listing.seller = request.user.profile
    listing.location = listing_location
    listing.save()
    messages.info(request, f'{listing.model} Listing Posted successfully')
    return redirect('home')

   else:
    raise Exception()
  except Exception as e:
   print(e)
   messages.error(request, 'error posting')
   return redirect('home')
 elif request.method == 'GET':
  listing_form = ListingForm()
  location_form = LocationForm()

  return render(request, 'views/list.html', {'listing_form':listing_form, 'location_form':location_form})


@login_required
def listting_view(request, id): #id was added as a positional agument
  try:
    listing1 = listing.objects.get(id=id)
    if listing1 is None:
      raise Exception
    return render(request, 'views/listing.html', {'listing1':listing1})
  except Exception as e:
    messages.error(request, f'Invalid UID {id} was provided for listing')
    return redirect('home')

 
