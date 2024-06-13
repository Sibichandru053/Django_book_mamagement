from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_page,name='login_page'),
    path('signup/',views.signup_page,name='signup_page'),
    path('book/booklist',views.book_list,name='book_list'),
    path('book/<int:pk>/',views.book_detail,name='book_detail'),
    path('book/now/',views.book_create,name='book_create'),
    path('book/<int:pk>/edit/',views.book_update,name='book_update'),
    path('book/<int:pk>/delete/',views.book_delete,name='book_delete'),
]