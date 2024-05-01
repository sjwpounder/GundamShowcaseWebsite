from django.urls import path

from . import views

app_name = 'collection'

urlpatterns = [
    path('', views.all_kits, name='all_kits'),
    path('item/<slug:slug>/', views.kit_detail, name='kit_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
]