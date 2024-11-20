from django.shortcuts import render,redirect
from app1.models import Movie
def home(request):
    m=Movie.objects.all()
    context={'movie':m}
    return render(request,'home.html',context)
def add(request):
    if(request.method=="POST"):
        t=request.POST['t']
        d=request.POST['d']
        l=request.POST['l']
        y=request.POST['y']
        i=request.FILES['i']

        m=Movie.objects.create(title=t,description=d,language=l,year=y,image=i)
        m.save()
        return redirect('home')


    return render(request,'addmovie.html')

def detail(request,p):
    m=Movie.objects.get(id=p)
    context={'movie':m}
    return render(request,'detail.html',context)

def delete(request,p):
    m=Movie.objects.get(id=p)
    m.delete()
    return redirect('home')