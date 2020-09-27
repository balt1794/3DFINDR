from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from listings.models import Customer
from .decorators import unauthenticated_user


@unauthenticated_user
def registerPage(request):
    if request.method != 'POST':
        form = CreateUserForm()
    else:
        form = CreateUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            Customer.objects.create(
                user=user,
            )
            return redirect('users:login')

    context = {'form': form}
    return render(request, 'users/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('listings:index')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'users/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('listings:index')
