from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import Category, Subcategory, Product


# Create your views here.
def index(request):
    return HttpResponse('Own Product Listing will be here...')

@login_required
def create_request(request):
    nbar = 'wanttosell'    
    all_category = Category.objects.all()
    data={
        'nbar':nbar,
        'categories': all_category
    }    
    return render(request, 'product/product_form.html', data)
