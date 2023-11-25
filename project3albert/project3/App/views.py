from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from App.models import*
from App.form import*


def home(request):
    return render(request,'base.html')
def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('pass1')
        password2=request.POST.get('cpass1')
        if password1==password2:
            if User.objects.filter(username=username,email=email).exists():
                    messages.info(request,'username already exists')
                    print("Already Have")
            else:
                new_user=User.objects.create_user(username,email,password1)
                new_user.save()
                print('success')
                return redirect(user_login)
        else:
            print("wrong password")
    return render(request,'signup.html')

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password1=request.POST.get('pass1')
        user=authenticate(request,username=username,password=password1)
        if user is not None:
            login(request,user)
            return redirect(home)
        else:
            messages.info(request,'user not exist')
            print('user not exist')
            return redirect(user_login)
    return render(request,'login.html')
        

def user_logout(request):
    logout(request)
    return redirect(user_login)

        

def add_book(request):
    #  form=bookform()
     if(request.method=='POST'):
          d=studentform(request.POST)
          if d.is_valid():
            d.save()
            return redirect(view_book)
     return render (request,'add_book.html')
def view_book(request):
    b=book.objects.all()
    return render (request,'list.html',{'book':b})
# def edit(request,a):
#     m=book.objects.get(pk=a)
#     form=studentform(instance=m)
#     if request.method=='POST':
#         form=studentform(request.POST,instance=m)
#         if form.is_valid():
#             form.save()
#             return home (request)
#     return render (request,"edit.html",{'form':form})
# def deleteitem(request,a):
#     m=book.objects.get(pk=a)
#     m.delete()
#     return render (request,'form1.html')
# def form1(request):
#     form=studentform()
#     if request.method=='POST':
#         form=studentform(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(form1)
#     return render (request,'form1.html')



# Create your views here.
