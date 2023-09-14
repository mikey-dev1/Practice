from django import forms

from .models import *

class ListingForm(forms.ModelForm):


 class Meta:
  model = listing
  fields = {'brand','model','vin','mileage','color','description','engine','transmission','image'}
  