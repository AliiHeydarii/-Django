from django.db import models
from accounts.models import CustomUser
from django.template.defaultfilters import slugify
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
    slug = models.SlugField()
    image = models.ImageField(upload_to='ads')
    title = models.CharField(max_length=250)
    description = models.TextField()
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    city = models.OneToOneField(City , on_delete=models.CASCADE)
    
    
    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)
    
    
    def __str__(self):
        return self.title