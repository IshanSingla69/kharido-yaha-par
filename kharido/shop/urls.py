from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shop_home'),
    path('about/', views.about, name='about_us'),
    path('contact/', views.contact, name='contact_us'),
    path('tracker/', views.tracker, name='tracker'),
    path('search/', views.search, name='search'),
    path('productview/', views.productView, name='productView'),
    path('checkout/', views.checkout, name='checkout'),
    
]
