from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin-signup/', views.admin_signup, name='admin_signup'),
     path('home/', views.home, name='home'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('books/', views.book_list, name='book_list'),
    path('add-book/', views.add_book, name='add_book'),
    path('edit-book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete-book/<int:book_id>/', views.delete_book, name='delete_book'),
]
