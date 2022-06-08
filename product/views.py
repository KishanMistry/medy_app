import code
from email.policy import default
from itertools import product
from math import prod
from unicodedata import category
from wsgiref.util import request_uri
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from product.models import Category, Subcategory, Product, Productimage
from product.forms import productForm
from django.contrib import messages
from django.db.models import FilteredRelation, Q, F

# Create your views here.
def index(request):
    # ################## Inner join ################
    # product_image = Productimage.objects.filter(default = 1, product__user_id = request.user.id)
    # context = { 'nbar' : 'myproducts', 'data' : product_image }
    # return render(request, 'product/product_list.html', context)

    # ################## Left Outer join ################
    product_image = Product.objects.filter(user_id = request.user.id).annotate( 
            pi=FilteredRelation('Productimage', condition=Q(Productimage__default=1)),
            pi_pic=F('pi__image_name')
        )    
    context = { 'nbar' : 'myproducts', 'data' : product_image }
    return render(request, 'product/product_list.html', context)

@login_required
def create_request(request):
    nbar = 'wanttosell'
    if request.method == "POST":
        form = productForm(request.POST)
        if form.is_valid():            
            pr_form = form.save(commit=False)
            pr_form.user = request.user            
            pr_form.save()
            images = request.FILES.getlist('images')
            for i, image in enumerate(images):
                if(i == 0): 
                    default = 1
                else:
                    default = 0
                Productimage.objects.create( image_name=image, product = pr_form, default = default )
            messages.success( request, "Product created successfully..!", extra_tags="alert-success")            
            return redirect('product')        
    else:
        form = productForm() 
    all_category = Category.objects.all()
    data={ 'nbar':nbar, 'categories': all_category, 'pr_form' : form }
    return render(request, 'product/product_form.html', data)

@login_required
def get_sub_category(request):
    # try:
    #     sub_categories = list(Subcategory.objects.filter(category_id = request.POST.get("category_id")).select_related('category').values())        
    # except Subcategory.DoesNotExist:
    #     raise Http404
    # return JsonResponse({
    #     'status': 'success',
    #     'data': sub_categories
    # })
    #=======
    sub_categories = list(Subcategory.objects.filter(category_id = request.POST.get("category_id")).select_related('category'))
    return JsonResponse({
        'status': 'success',
        'data': [{'id': sc.id, 'sub_category_name': sc.sub_category_name, 'category': sc.category.category_name, 'cat_id': sc.category.id} for sc in sub_categories],
    })   

def product_edit(request, slug):
    nbar = 'myproducts'   
    try:
        product = Product.objects.get(slug = slug, user_id = request.user.id)
        if request.method == "POST":            
            form = productForm(request.POST, instance=product)
            if form.is_valid():
                pr_form = form.save(commit=False)
                pr_form.user = request.user            
                pr_form.save()
                images = request.FILES.getlist('images')
                for i, image in enumerate(images):
                    if(i == 0): 
                        default = 1
                    else:
                        default = 0
                    Productimage.objects.create( image_name=image, product = pr_form, default = default )
                messages.success( request, "Product Updated successfully..!", extra_tags="alert-success")            
                return redirect('product')
        else:        
            form = productForm(instance=product)        
        all_category = Category.objects.all()
        data={ 'nbar':nbar, 'categories': all_category, 'pr_form' : form, 'action':'edit', 'product':product }
        return render(request, 'product/product_form.html', data)        
    except Product.DoesNotExist:
        raise Http404