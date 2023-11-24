from django.shortcuts import render
from django.http import HttpResponse
from App1.models import*
def home(request):
    return HttpResponse("dghdfddfg")
def add(request):
    return render(request,'home.html')
def home(request):
    d={'name':'sam','age':20}
    return render(request,'home.html',d)
from App1.models import*
def home(request):
    d=student.objects.all()
    return render(request,'home.html',{'t':d})
from App1.form import*
def form1(request):
        form=studentform()
        if(request.method=='POST'):
             form=studentform(request.POST)
             if (form. is_valid()):
                  form.save()
                  return home (request)
        return render(request,'form1.html',{'form':form})
        


# Create your views here.
