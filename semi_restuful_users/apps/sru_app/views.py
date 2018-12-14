from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import *
# Create your views here.
def index(request):
    return render(request, "sru_app/index.html", {"users": User.objects.all()})

def new(request):

    return render(request, "sru_app/new.html")

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        user = User.objects.get(first_name=request.POST['first_name'])
        return redirect(f'users/{user.id}')

def update(request):
    errors = User.objects.basic_validator(request.POST)
    id = request.POST['id']
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect(f'users/{id}/edit')
    else:
        user = User.objects.get(id = request.POST['id'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect(f'users/{user.id}')

def show(request, id):
    return render(request, "sru_app/show.html", { "user": User.objects.get(id = id)} )

def edit(request, id):
    return render(request, "sru_app/edit.html", { "user": User.objects.get(id = id)} )

def delete(request, id):
    b = User.objects.get(id = id)
    b.delete()
    return redirect('/')
