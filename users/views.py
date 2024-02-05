from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignupForm


# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'users/signup.html', {'form': form})
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})


# login page
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid email or password. Please try again.')
                return render(request, 'users/login.html', {'form': form})
        else:
            # Form is not valid, handle errors
            messages.error(request, 'Invalid form submission. Please check the form data.')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


# logout page
def user_logout(request):
    logout(request)
    return redirect('login')
