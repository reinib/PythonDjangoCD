from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):

    return render(request, "survey/index.html")

def result(request):

    if "count" not in request.session:
        request.session["count"] = 0
    request.session["count"] += 1

    name = "N/A"
    if 'name' in request.POST:
        name = request.POST["name"]
    comment = "N/A"
    if 'comment' in request.POST:
        comment = request.POST["comment"]

    context = {
        'name' : name,
        'location' : request.POST["location"],
        'favLang' : request.POST["favLang"],
        'comment' : comment
    }

    return render(request, "survey/result.html", context)

def back(request):

    return redirect('/')
