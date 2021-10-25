
from django.urls import path 
from Home import views

urlpatterns = [
    path('',  views.index ,  name = "index" ) ,
    path('base',  views.base , name = "base" ) ,
    path('order',  views.order , name = "order" ) ,
    path('login',  views.login , name = "login" ) ,
    path('checkout',  views.checkout , name = "checkout" ) ,
]