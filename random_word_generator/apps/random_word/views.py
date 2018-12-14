from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):

    return render(request,'random_word/index.html')

def create(request):
    print(request.method)
    print(request.POST)

    if "count" not in request.session:
        request.session["count"] = 0
    request.session["count"] += 1


    word = get_random_string(length=14)
    request.session["word"] = word

    return redirect('/')

def reset(request):

    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]

    return redirect('/')
