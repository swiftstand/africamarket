#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sulaiman maryam
#
# Created:     18-05-2020
# Copyright:   (c) sulaiman maryam 2020
# Licence:     <your licence>

from django.urls import path
from . import views
from .views import AdminPostListView,AdminPostDetailView

urlpatterns = [
    path('',views.home, name='amweb-home'),
    path('adminposts/',AdminPostListView.as_view(), name='adminposts'),
    path('adminposts/<str:slug>/',AdminPostDetailView.as_view(), name='adminpost_detail'),
    path('accounts/', views.accounts, name= 'amweb-accounts'),
    path('about/', views.about, name= 'amweb-about'),
    path('contactus/', views.contactus, name= 'amweb-contactus'),
    path('our-services/', views.service, name= 'amweb-services'),
    path('cart/', views.cart, name= 'amweb-cart'),
    path('checkout/', views.checkout, name= 'amweb-checkout'),
    path('wishlist/', views.wishlist, name= 'amweb-wishlist'),
]