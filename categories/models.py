from django.utils.html import format_html
from django.db import models

class Categories(models.Model):
    category_name = models.CharField(max_length=100, null=False, unique=True)
    description = models.TextField(max_length=600, null=True)
    image = models.ImageField(upload_to='category')
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.category_name
    
    class Meta:
        db_table = 'categories'

    def image_tag(self):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(url = self.image.url, width='60px', height='60px'))                
    
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
        

