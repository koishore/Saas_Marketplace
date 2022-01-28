from django.urls import path

from . import views

urlpatterns =[
    path('', views.index),
    path('login', views.login),
    path('receive', views.receive),
    path('seller_home',views.seller_home, name="seller_home")
]
