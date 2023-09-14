from django.urls import path
from .views import *



urlpatterns = [
    path('', landing_view, name='main' ),
    path('new', new_page, name='new'),
    path('home', home_view, name = 'home'),
    path('list',  list_view, name="list"),
    path('listing/<str:id>/', listting_view, name="listing"),
]
