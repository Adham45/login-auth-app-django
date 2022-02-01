from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        request.session['username'] = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/home')
        else:
            messages.info(request, 'invalid username or password')
            return redirect("/")
    else:
        return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(username=username, password=password, email=email, is_staff=True)
        user.save()
        print('user created')
        return redirect('/custom')

    return render(request, 'register.html')


def custom(request):
    return render(request, 'custom.html')


def home(request):
    return render(request, 'home.html')
