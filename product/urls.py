
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [    
    path("", views.index, name='product'),
    path("/add", views.create_request, name='product/add'),
    path("/get_sub_category", views.get_sub_category, name='product/get_sub_category')
    
]