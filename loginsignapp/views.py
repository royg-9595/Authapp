from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login

def home(request):
    return render(request, "crudapp/index.html")
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        
        firstname=request.POST['firstname']
        
        lastname=request.POST['lastname']

        email=request.POST['email']
        password=request.POST['password']
        pass2=request.POST['pass2']
        
        myuser=User.objects.create_user(username, email, password)
        myuser.first_name= firstname
        myuser.last_name= lastname
        
        myuser.save()
        
        messages.success(request, "Account Created ╰(*°▽°*)╯")
        
        return redirect('signin')
        
        
    
    return render(request, "crudapp/signup.html")
def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request,user)
            fname1= user.last_login
            return render(request, "crudapp/index.html",{'fname':fname1} )
        else:
            messages.error(request,"Incorrect Credentials")
            return redirect('home')
    return render(request, "crudapp/signin.html")
def signout(request):
    pass


# Create your views here.
