from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.data.apyori_algo import *

# Create your views here.
def index(request):
    dict_products = list_items.copy()
    return render(request, 'index.html', {'dict_products': dict_products})

def suggest(request):
    if request.method == 'POST':
        bought_products = request.POST.getlist('product')
        if bought_products:
            should_products = Suggest(bought_products)
            return render(request, 'suggest.html', {'products' : should_products})
        else:
            return redirect('index')
