# from email import message
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, RegistrationUserEmail
# from .forms impor

# Create your views here.
def loginUser(request):
    title = "Login"
    form = LoginForm(request.POST or None)
    context={
        'form':form,
        'title': title,
    }
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password = password)

            login(request, user)
            return redirect('index')
        else:
            messages.warning(request,form.errors)
            messages.error(request, 'Invalid username or password')
            print(form.errors)
            return redirect('login')
    else:
        return render(request, 'authentication/login.html', context=context)

def register(request):
    title = "Create Account"
    if request.method == "POST":
        form = RegistrationUserEmail(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            form.save()
            password = form.cleaned_data.get('password1')
            # login user after signing up
            user = authenticate(username= user.username, password = password)
            login(request, user)
            return redirect('login')
        else:
            messages.info(request, form.errors)
            return redirect('register')
    else:
        form = RegistrationUserEmail()
        context = {'form': form, 'title': title}
        return render(request, 'authentication/register.html', context=context)


def logoutUser(request):
    logout(request)
    return redirect('index')