from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

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
        myuser.firstname= firstname
        myuser.lastname= lastname
        
        myuser.save()
        
        messages.success(request, "Account Created ╰(*°▽°*)╯")
        
        return redirect('signin')
        
        
    
    return render(request, "crudapp/signup.html")
def signin(request):
    return render(request, "crudapp/signin.html")
def signout(request):
    pass


# Create your views here.
