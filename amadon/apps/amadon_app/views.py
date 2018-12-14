from django.shortcuts import render, HttpResponse, redirect

from .models import *
# Create your views here.
def index(request):

    return render(request, "amadon_app/index.html", {"items": Item.objects.all().values()})

def buy(request):
    # amount = (Item.objects.get(id=request.POST['product_id']) * request.POST['quantity'])
    item = Item.objects.get(id=request.POST['product_id'])
    price = item.price
    amount = float(price) * float(request.POST['quantity'])
    # print(request.POST['quantity'])
    # print(amount)
    request.session['amount'] = amount

    if "num_items" not in request.session:
        request.session["num_items"] = request.POST['quantity']
    else:
        request.session["num_items"] += request.POST['quantity']

    # insert purchase into user model
    user = User.objects.get(id=1)
    for i in range(int(request.POST['quantity'])):
        user.items.add(Item.objects.get(id=request.POST['product_id']))

    return redirect('/purchase')

def purchase(request):
    return render(request, "amadon_app/checkout.html")
