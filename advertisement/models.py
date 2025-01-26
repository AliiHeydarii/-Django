from django.db import models
from accounts.models import CustomUser
from slugify import slugify
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
    
class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    # slug = models.SlugField()
    image = models.ImageField(upload_to='ads')
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=15 , decimal_places=3)
    description = models.TextField()
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE , blank=True , null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    city = models.ForeignKey(City , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
   
    def __str__(self):
        return self.title