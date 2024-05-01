from django.shortcuts import render,request
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Product

class ProductList(request):
    dict = {'product':Product}
    return render(request, 'products/list.html', context=dict)