from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
def index(request):
    if request.method=='POST':
        form=Studform(request.POST)
        if form.is_valid():
            form.save()
            print("record inserted:")
        else:
            print("form.errors")
    return render(request,'index.html')


def showdata(request):
    stdata=stud.objects.all()
    return render(request,'showdata.html',{'stdata':stdata})
def deletedata(request,id):
    stid=stud.objects.get(id=id)
    stud.delete(stid)
    return redirect('showdata')
def update(request,id):
    stid=stud.objects.get(id=id)
    if request.method=='POST':
        form=Studform(request.POST,instance=stid)
        if form.is_valid():
            form.save()
            print("Record updated!")
            return redirect('showdata')
        else:
            print(form.errors)
    return render(request,'update.html',{'stid':stid})