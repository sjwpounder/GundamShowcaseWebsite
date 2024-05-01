from django.shortcuts import get_object_or_404, render

from .models import Category, Kit

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def all_kits(request):
    kits = Kit.objects.all()
    return render(request, 'collection/home.html', {'kits': kits})

def kit_detail(request, slug):
    kit = get_object_or_404(Kit, slug=slug)
    return render(request, 'collection/kits/detail.html', {'kit': kit})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    kits = Kit.objects.filter(category=category)
    return render(request, 'collection/kits/category.html', {'category': category, 'kits': kits})