# from django.conf.urls import include, re_path
from django.contrib import admin
from django.urls import path, include

from api.views import products_list, categorys_list, product_details, category_details
# from api.models import Product, Category


urlpatterns=[
    path('products/', products_list),
    path('products/<int:product_id>', product_details),
    path('categorys/', categorys_list),
    path('categorys/<int:category_id>', category_details),
]
