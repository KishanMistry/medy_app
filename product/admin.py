from django.contrib import admin
from django.contrib import admin
from product.models import Category, Product, Productimage, Subcategory
from django.utils.html import escape
from django.utils.html import format_html


# class AdminCategory(admin.ModelAdmin):
#     model = Category
#     list_display = ['category_name', 'image_tag', 'description'] # Ordering of fields in admin listing    
#     fields = ['category_name', 'description', 'image'] # Ordering of fields in admin form
#     readonly_fields = ['image_tag']

# admin.site.register(Category, AdminCategory)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Productimage)
admin.site.register(Subcategory)