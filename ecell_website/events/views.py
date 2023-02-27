from django.shortcuts import render
from .forms import Friend_Form
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    return render(request, "friends/index.html", {})

def register(request):
    submitted = False
    if request.method == 'POST':
        submitted = False
        form=Friend_Form(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/register?submitted=True')
    else:
        form=Friend_Form
        if 'submitted' in request.GET:
            submitted = True
    return render(request,"friends/Register_user.html",{'form':form,'submitted':submitted})
def startup(request):
    return render(request, "friends/startup.html", {})

def members(request):
    return render(request, "friends/members.html", {})

def events(request):
    return render(request, "friends/events.html", {})

def gallery(request):
    return render(request, "friends/gallery.html", {})