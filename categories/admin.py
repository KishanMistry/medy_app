from django.contrib import admin
from django.contrib import admin
from categories.models import Categories
from django.utils.html import escape
from django.utils.html import format_html


class AdminCategory(admin.ModelAdmin):
    model = Categories
    list_display = ['category_name', 'image_tag', 'description'] # Ordering of fields in admin listing    
    fields = ['category_name', 'description', 'image'] # Ordering of fields in admin form
    readonly_fields = ['image_tag']

admin.site.register(Categories, AdminCategory)