from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt

from .models import *

# Create your views here.
def index(request):
    return render(request, "log_regs_app/index.html")

def validate_register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        b = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=password)
        b.save()
        messages.success(request, "Successfully registered!")
        user = b
        # request.session['user_name'] = User.objects.filter(first_name=request.POST['first_name']).first_name.values()

        return redirect(f'users/{user.id}')

def validate_login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        user = User.objects.get(email=request.POST['email'])
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            messages.success(request, "Successfully logged in!")
            return redirect(f'users/{user.id}')
        else:
            return redirect('/')

def success(request, id):
    return render(request, "log_regs_app/success.html", {"user": User.objects.get(id = id)})
