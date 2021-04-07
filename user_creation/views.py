from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from user_creation.models import user_data
from user_creation.forms import singup_form
from django.core.files.storage import FileSystemStorage


# Create your views here.
def index(request):

   
    return render(request, 'index.html')

def registration(request):
    
    form = singup_form(request.POST)
    if form.is_valid():
        print(form.is_valid())
        user = form.save()
        user.set_password(user.password)
        user.save()
        messages.info(request,'user created')
        return redirect('login')

    context = {'form' : form  }
    return render (request,"registration.html", context)

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid Username/Password')
            return redirect('login')
        
    else:
        return render(request,'login.html')

    

def logout(request):
    auth.logout(request)
    return redirect('/')

