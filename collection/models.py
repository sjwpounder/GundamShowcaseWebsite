from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


#Defining a table for Django to create for the categories. Includes name, slug, plural override
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True) #slug is what's typed into the address bar

    class Meta:
        verbose_name_plural = 'categories' #overrides default plural name

    def get_absolute_url(self):
        return reverse('collection:kit_detail', args=[self.slug])

    def __str__(self):
        return self.name


#Defining a table for the kits. Has a link to the category table using a category FK, associating category to product.
class Kit(models.Model):
    category = models.ForeignKey(Category, related_name='kit', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='kit_creator', on_delete=models.CASCADE)
    kitname = models.CharField(max_length=255) #name of kit
    series = models.TextField(blank=True)  #series kit is from
    manufacturer = models.CharField(max_length=255, default='admin')    #manufacturer of kit (Bandai, Kotobukia etc)
    description = models.TextField(blank=True)  #description of kit. More info
    image = models.ImageField(upload_to='images/')  #one image for now. This is a link to the image
    slug = models.SlugField(max_length=255)
    built = models.DateTimeField(blank=True) #date kit was built
    created = models.DateTimeField(auto_now_add=True)   #when page was created
    updated = models.DateTimeField(auto_now=True)   #when page was last updated

    class Meta:
        verbose_name_plural = 'Kits'    #not really needed but here for clarity
        ordering = ("-created",)    #ordering list on descending order. Latest added at top

    def get_absolute_url(self):
        return reverse('collection:kit_detail', args=[self.slug])
    

    def __str__(self):
        return self.kitname  #returning kit name by default
