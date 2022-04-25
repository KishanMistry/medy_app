from unicodedata import category
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from product.models import Category, Subcategory, Product
from product.forms import productForm
from django.contrib import messages

# Create your views here.
def index(request):
    data = Product.objects.all()
    return render(request, 'product/product_list.html', {'products' : data})

@login_required
def create_request(request):
    nbar = 'wanttosell'
    if request.method == "POST":
        form = productForm(request.POST)
        if form.is_valid():            
            form = form.save(commit=False)            
            form.save()
            messages.success( request, "Product created successfully..!", extra_tags="alert-success")
            return redirect("product")
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