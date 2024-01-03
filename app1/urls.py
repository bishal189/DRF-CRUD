from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('book/',views.Book_list,name='book'),
    path('bookdetail/<int:pk>',views.Bookdetails,name='bookdetails'),
    # 
   
]