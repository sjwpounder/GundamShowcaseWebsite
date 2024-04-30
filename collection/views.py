from django.shortcuts import render

from .models import Category, Kit

def all_kits(request):
    kits = Kit.objects.all()
    return render(request, 'collection/home.html', {'kits': kits})
