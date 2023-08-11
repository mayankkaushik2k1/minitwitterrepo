from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout




def home(request):
    return render(request,'users/index.html')  
    #import pdb
    #pdb.set_trace()
    #return HttpResponse('welcome to twitter')

def signup(request):
    if request.method == 'POST':
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

    return render(request, 'users/signup.html')



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
