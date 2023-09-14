from django.contrib import admin
from .models import listing

class ListingAdmin(admin.ModelAdmin):
 pass

admin.site.register(listing, ListingAdmin)
