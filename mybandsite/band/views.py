from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Member, Event
from django.contrib.auth.models import User




@login_required(login_url='login')
def home(request):
    """ This return to home
    
        :param request request: Client HTTP request
        
        :returns: home template
        
        :rtype: HTML document
    """
    return render(request, 'home.html')


def members(request):
    """ This return to members
    
        :param request request: memeber list
        
        :returns: member template
        
        :rtype: HTML document
    """
    members_list = Member.objects.all()
    return render(request, 'members.html', {'members': members_list})


def events(request):
    """ This return to event
    
        :param request request: event
        
        :returns: event template
        
        :rtype: HTML document
    """
    events_list = Event.objects.all()
    return render(request, 'events.html', {'events': events_list})


def login_user(request):
    """ This return to login
    
        :param request request: Clogin
        
        :returns: login. template
        
        :rtype: HTML document
    """
    return render(request, 'login.html')


def authenticate_user(request):
    """ This return to authenticate user
    
        :param request request: User authentication
        
        :returns: login.html or home view
        
        :rtype: HTML document or python function
    """
    username = request.POST.get("username")
    password = request.POST.get("password")
    
    user = authenticate(username=username, password=password)
    if user is None:
        error_message = "Invalid Username or Password!"
        return render(request, "login.html", {'error_message': error_message})
    else:
        login(request, user)
        return HttpResponseRedirect(reverse("home"))

def reg_user(request):
    """ This return to user registration
    
        :param request request: registering user
        
        :returns: register.html
        
        :rtype: HTML document or python function
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
        # Create a New User & Save to Database
            try:
                user = User.objects.create_user(username=username, password=password)
                user.is_staff = False
                user.is_superuser = False
                # Save user to Db
                user.save()
                # Redirect user
                return HttpResponseRedirect(reverse('home'))
            except Exception as ex:
                print(f'SOMETHING WENT WRONG!\nError:\n{str(ex)}')
                return render(request, 'register.html', {'error_message': str(ex)})
    # Redirect User - create_new_user
    return render(request, 'register.html')


def logout_user(request):
    """ This return to logout
    
        :param request request: user logout
        
        :returns: login template
        
        :rtype: HTML document
    """
    logout(request)
    return render(request, 'login.html')

