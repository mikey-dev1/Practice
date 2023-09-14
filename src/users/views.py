from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib.auth.decorators import login_required

def login_view(request):
 if request.method == 'POST':
  login_form = AuthenticationForm(request=request, data=request.POST) 
  if login_form.is_valid():
   username = login_form.cleaned_data.get('username')                      
   password = login_form.cleaned_data.get('password')
   user = authenticate(username= username, password=password)
   if user is not None:
    login(request, user)
    messages.success(request, f'thumbs up bro you are now logged in successfully mr {username}')
    return redirect('home')
   else:
    pass

 elif request.method == 'GET':
  login_form = AuthenticationForm()
 return render(request, 'views/login.html', {'login_form': login_form})

@login_required
def logout_view(request):
   logout(request)
   return redirect('main')

class registerView(View):
   def get(self, request):
      register_form = UserCreationForm
      return render(request, 'views/register.html', {'register':register_form})
   def post(self, request):
      register_form = UserCreationForm(data=request.POST)
      if register_form.is_valid():
         user = register_form.save()
         user.refresh_from_db()
         login(request, user)
         messages.success(request, f"congratulations mr {user.username}")
         return redirect('home')
      else:
         messages.error(request, f'oops error from your signup')
         return render(request, 'views/register.html', {'register':register_form})

