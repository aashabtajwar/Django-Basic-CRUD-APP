from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'LOGGED IN!')
            return redirect('blog-home')
        else:
            messages.success(request, 'Username or Password is incorrect')
    return render(request, 'users/login.html')

def logoutUser(request):
    logout(request)
    messages.success(request, 'Logged Out')
    return redirect('user-login')

def register(request):
    if request.method == 'POST':
        # if the request is POST
        # we will create a form that 
        # has the POST data in it
        form = UserRegisterForm(request.POST)
        # now this form has the data that we submitted
        # however, we are still going to validate it
        # so that we can know for sure that we are getting
        # the data that we are expecting
        if form.is_valid():
            form.save() # this automatically saves the user
                        # in the database with its password hashed
            # if valid
            username = form.cleaned_data.get('username')
            # now using flash message to show that
            # we received valid data
            messages.success(request, f'Account created for {username}!')
            # now redirecting user to a different page
            return redirect('blog-home')


    else:
        # else we create an empty form
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})
"""
    messages.debug
    messages.info
    messages.success
    messages.warning
    messages.error
"""