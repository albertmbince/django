from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import user,auth 
def home (request):
    return render(request,'home.html')
def register(request):
    if request.method=='POST':
        first_name=request.POST('first_name')
        last_name=request.POST('last_name')
        username=request.POST('username')
        email=request.POST('email')
        password=request.POST('password')
        confirm_password=request.POST('confirm_password')
        if password==confirm_password:
            if user.objects.filter(username=username).exists():
                messages.info(request,'Email exists')
                return redirect(register)
        else:
            messages.info(request,'Both passwords are not matching')
            return redirect (register)
    else:
        print("no post method")
        return render(request,'register.html')
def login_user(request):
     if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid username or password')
            return redirect('login_user')
     else:
         return render(request,'login.html')
def logout_user(request):
    auth.logout(request)
    return redirect('home')
            
# Create your views here.
