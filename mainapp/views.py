from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import ToDoList,Item
from .forms import CreateNewList

# Create your views here.
def index(response,id):
    ls=ToDoList.objects.get(id=id)
    return render(response,"mainapp/list.html",{"ls":ls}) #dictionary of variables,key can be used in html to call value dynamically

def home(response):
    return render(response,"mainapp/home.html",{})

def create(response):
    
    if response.method=="POST":
        form=CreateNewList(response.POST)
        if form.is_valid():
            n=form.cleaned_data["name"]
            t=ToDoList(name=n)
            t.save()
            return HttpResponseRedirect("/%i" %t.id) 
    else:
        form=CreateNewList()        
    
    return render(response,"mainapp/create.html",{"form":form})





