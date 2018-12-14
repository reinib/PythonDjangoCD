from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
# Create your views here.
def index(request):
    context = {
        "date": strftime("%Y-%m-%d", gmtime()),
        "time": strftime("%H:%M %P", gmtime())
    }
    return render(request,'times/index.html', context)
