#-------------------------------------------------------------------------------
# Name:        urls
# Purpose:     inventory
#
# Author:      sulaiman maryam
#
# Created:     10-06-2020
# Copyright:   (c) sulaiman hammed swift 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------


from django.urls import path
from . import views
from .views import (ItemsFiveListView,ItemsFourListView,ItemsThreeListView,ItemsTwosListView,ItemsOneListView,
                    FilterOne,FilterThree,FilterFour,FilterFive,FilterTwo,
                    ItemShelfOneCreate,ItemShelfTwoCreate,ItemShelfThreeCreate,ItemShelfFourCreate,ItemShelfFiveCreate
                    )

urlpatterns = [
    path('item/<str:store_name>-<int:pk>-<str:slug>/',ItemsOneListView.as_view(), name='itemsone'),
    path('preitem/<str:store_name>-<int:pk>-<str:slug>/',ItemsTwosListView.as_view(), name='itemstwo'),
    path('2preitem/<str:store_name>-<int:pk>-<str:slug>/',ItemsThreeListView.as_view(), name='itemsthree'),
    path('diaitem/<str:store_name>-<int:pk>-<str:slug>/',ItemsFourListView.as_view(), name='itemsfour'),
    path('2diaitem/<str:store_name>-<int:pk>-<str:slug>/',ItemsFiveListView.as_view(), name='itemsfive'),
    path('status/<str:slug>-<str:store_name>-<int:pk>-<str:status>/',FilterOne.as_view(), name='filterone'),
    path('prestatus/<str:slug>-<str:store_name>-<int:pk>-<str:status>/',FilterTwo.as_view(), name='filtertwo'),
    path('2prestatus/<str:slug>-<str:store_name>-<int:pk>-<str:status>/',FilterThree.as_view(), name='filterthree'),
    path('diastatus/<str:slug>-<str:store_name>-<int:pk>-<str:status>/',FilterFour.as_view(), name='filterfour'),
    path('2diastatus/<str:slug>-<str:store_name>-<int:pk>-<str:status>/',FilterFive.as_view(), name='filterfive'),
    path('item/new/<str:slug>-<str:shelf_name>/',ItemShelfOneCreate.as_view(), name='createitemone'),
    path('preitem/new/<str:slug>-<str:shelf_name>/',ItemShelfTwoCreate.as_view(), name='createitemtwo'),
    path('2preitem/new/<str:slug>-<str:shelf_name>/',ItemShelfThreeCreate.as_view(), name='createitemthree'),
    path('diaitem/new/<str:slug>-<str:shelf_name>/',ItemShelfFourCreate.as_view(), name='createitemfour'),
    path('2diaitem/new/<str:slug>-<str:shelf_name>/',ItemShelfFiveCreate.as_view(), name='createitemfive'),
    ]