from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime

# Create your views here.
def index(request):

    if "gold" not in request.session:
        request.session["gold"] = 0

    if "activities" not in request.session:
        request.session["activities"] = []

    return render(request,"ninja_gold_app/index.html")


def process(request):

    context = {
        "arena": request.POST["arena"],
        "time": strftime("%Y-%m-%d %Y-%m-%d", gmtime())
    }

    # process money from the farm
    print(request.POST["arena"])
    if request.POST["arena"] == "farm":
        amount = int(random.randrange(10,21))

    # process money form the cave
    elif request.POST["arena"] == "cave":
        amount = int(random.randrange(5,11))

    # process money from the house
    elif request.POST["arena"] == "house":
        amount = int(random.randrange(2,5))

    # process money from the casino
    elif request.POST["arena"] == "casino":
        print("true")
        amount = int(random.randrange(-50,50))

    request.session["gold"] += amount

    if amount < 0:
        print("no more money!!")
        request.session["activities"].append({"color":"red", "msg":"You entered the Casino and lost {} golds... OUCH!  {}".format(str(amount), context["time"])})
        return redirect('/')
        
    else:
        request.session["activities"].append({"color":"green", "msg": "You entered the {} and won {} golds! Yaayyy!!!!  {}".format(context["arena"], str(amount), context["time"])})


        return redirect('/')

def clear(request):

    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]

    return redirect('/')
