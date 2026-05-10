from django.contrib import admin
from django.urls import path,include
from newapp import views

urlpatterns = [
   path('',views.index),
   path('showdata/',views.showdata,name='showdata'),
   path('deletedata/<int:id>',views.deletedata),
   path('update/<int:id>',views.update),
]