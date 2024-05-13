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
        msg='email already exist'
        return render(request,'home.html',{'key':msg})
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
    data={
        'ddata':ddata
    }
    return render(request,'showdata.html',data)

def edit(request,pk):
    eddit=Student.objects.get(id=pk)
    return render(request,'update.html',{'eddit':eddit})

def update(request,pk):
    student=Student.objects.get(id=pk)
    if request.method=='POST':
        student.Firstname=request.POST.get('Firstname')
        student.Lastname=request.POST.get('Lastname')
        student.Email=request.POST.get('Email')
        student.City=request.POST.get('City')
        student.Contact=request.POST.get('Contact')
        student.save()
        msg="data updated"
        return redirect('showdata')
    return render(request,'update.html',{'student':student})

def delete(request,pk):
    sdel=Student.objects.get(id=pk)
    sdel.delete()
    msg="data deleted"
    return redirect('showdata')

    
    
        


