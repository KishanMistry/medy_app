from django.utils.html import format_html
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=100, null=False, unique=True)
    description = models.TextField(max_length=600, null=True)
    image = models.ImageField(upload_to='category', null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'categories'

    def image_tag(self):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(url=self.image.url, width='60px', height='60px'))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class Subcategory(models.Model):
    sub_category_name = models.CharField(
        max_length=100, null=False, unique=True)
    category = models.ForeignKey(
        Category, related_name="Subcategory", on_delete=models.CASCADE)
    description = models.TextField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True)

    @property
    def main_product_image(self):
        return self.Productimage.filter(default='Main Product Image').first()

    def __str__(self):
        return self.sub_category_name

    class Meta:
        db_table = 'sub_categories'


class Product(models.Model):
    title = models.CharField(max_length=100, null=False)
    slug = models.SlugField(max_length=120, unique=True)
    category = models.ForeignKey(Category, related_name="product_category", on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, related_name="product_sub_category", on_delete=models.CASCADE)
    description = models.CharField(max_length=100, null=False)
    buying_price = models.FloatField(default=0)
    selling_price = models.FloatField(default=0)
    buying_year = models.IntegerField(null=True)
    user = models.ForeignKey(User, related_name="user_product", on_delete=models.CASCADE, null=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'products'


class Productimage(models.Model):
    PLACEHOLDER= (
        ('Main Product Image', 'Main Product Image'),
        ('Sub Img 1', 'Sub Img 1'),
        ('Sub Img 2', 'Sub Img 2'),
    )
    product = models.ForeignKey(Product, related_name="Productimage", on_delete=models.CASCADE)
    image_name = models.ImageField(upload_to='product')
    default = models.CharField(max_length=20, choices=PLACEHOLDER)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.image_name.url

    class Meta:
        db_table = 'product_images'
