from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import redirect
# Create your views here.
def home(request):
    context={}
    context['form']=StudentForm
    return render(request,'home.html',context)

def insert(request):
    fname=request.POST.get('Firstname')
    lname=request.POST.get('Lastname')
    email=request.POST.get('Email')
    city=request.POST.get('City')
    contact=request.POST.get('Contact')
    data=Student.objects.filter(Email=email)
    print(data)

    if data:
        # msg='email already exist'
        return render(request,'home.html')
    else:
        Student.objects.create(Firstname=fname,
                               Lastname=lname,
                               Email=email,
                               City=city,
                               Contact=contact)
        # mmsg='suuccess'
        return render(request,'home.html')
    

def showdata(request):
    ddata=Student.objects.all()
    return render(request,'showdata.html',{'ddata':ddata})

    
        


