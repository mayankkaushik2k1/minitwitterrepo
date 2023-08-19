
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.urls import reverse
from .forms import SignUpForm , LoginForm




def home(request):
    return render(request,'users/home.html')  
    #import pdb
    #pdb.set_trace()
    #return HttpResponse('welcome to twitter')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            #user.refresh_from_db()
            #user.profile.email = form.cleaned_data.get('email')
            #user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect(reverse('home'))
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    return redirect('users:signup')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

    
    ''' if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request,'Username alraedy exists please try another username')
            return redirect('home')
        
        if User.objects.filter(email=email):
            messages.error(request, 'email alraedy registerd')
            return redirect('home')
        
        if len(username)>10:
            messages.error('username must be under 10 characters')

        if pass1 != pass2:
            messages.error(request,'Password did not match')

        if not username.isalnum():
            messages.error(request, 'username must be alphanumeric')
            return redirect('home')        

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, 'Your account is successfully created')

        return redirect('signin')
'''
   # return render(request, 'users/signup.html')


'''
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "users/index.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')





    return render(request,'users/signin.html')


def signout(request):
    logout(request)
    messages.success(request, 'logged out successfully')
    return redirect('home')
    #return render(request,'signout/signout.html')
# Create your views here.
'''
