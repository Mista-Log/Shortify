from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import URL, generate_short_code
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import get_object_or_404



def loginPage(request):

    # if request.user.is_authenticated:
    #     return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')


        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')




    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def signupUser(request):


    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'This username already exist')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'User was created successfully')
            user = authenticate(request, username=username, email=email, password=password)
            login(request, user)
            return redirect('home')
    return render(request, 'signup.html')


def homepage(request):
    short_url = None
    short_code = generate_short_code()
    
    if request.user.is_authenticated:
        user = request.user
    else:
        user = ''
    
    if request.method == 'POST':
        original_url = request.POST.get('url')
        url, created = URL.objects.get_or_create(original_url=original_url)
        if not created:
            short_code = url.short_code
        else:
            short_code = generate_short_code()
            url.short_code = short_code
            url.save()

        short_url = request.build_absolute_uri('/') + short_code



    context = {'user': user, 'short_url': short_url, 'short_code': short_code}
    return render(request, 'homepage.html', context)


def newUrl(request, short_code):
    url = get_object_or_404(URL, short_code=short_code)
    return redirect(url.original_url)