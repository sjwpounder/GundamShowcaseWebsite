from django.contrib import admin

from .models import Category, Kit

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Kit)
class KitAdmin(admin.ModelAdmin):
    list_display = ['name', 'manufacturer', 'series', 'slug', 'built', 'created', 'updated']
    list_filter = ['manufacturer', 'series']
