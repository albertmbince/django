from django.shortcuts import render
from App.models import*
from App.form import*

# Create your views here.
def home(request):
    return render(request,'base.html')
def upload(request):
    form=bookform()
    if(request.method=='POST'):
        form=bookform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return home (request)
    return render (request,'add.html',{'form':form})
def booklist(request):
        b=Book.objects.all()
        return render(request,'list.html',{'b':b})

def edit(request,p):
     m=Book.objects.get(pk=p)
     form=bookform(instance=m)
     if request.method=='POST':
          form=bookform(request.POST,request.FILES,instance=m)
          if form.is_valid():
               form.save()
               return home(request)
     return render(request,'edit.html',{'form':form})
def item_delete(request,p):
     m=Book.objects.get(pk=p)
     m.delete()
     return booklist(request)