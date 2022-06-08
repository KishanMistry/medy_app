from django import forms
from django.forms import ModelForm
from product.models import Category, Subcategory, Product
from django.contrib.auth.models import User

# Product form.
class productForm(ModelForm):
    title = forms.CharField(required=True)    
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":3}), required=True)
    buying_price = forms.CharField(required=False)
    selling_price = forms.CharField(required=True)
    buying_year = forms.CharField(required=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.HiddenInput(attrs={"id" : "cat_id"}))
    subcategory = forms.ModelChoiceField(queryset=Subcategory.objects.all(), widget=forms.HiddenInput(attrs={"id" : "sub_cat_id"}))    
    
    class Meta:
        model = Product
        fields = ["title", "category", "subcategory", "description", "buying_price", "selling_price", "buying_year"]