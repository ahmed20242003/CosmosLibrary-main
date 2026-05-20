"""
URL configuration for cosmos_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import page_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    
    # Frontend Pages
    path('', page_views.index, name='index'),
    path('login/', page_views.login_page, name='login_page'),
    path('dashboard/', page_views.dashboard, name='dashboard'),
    path('books/', page_views.books, name='books'),
    path('book-details/<int:book_id>/', page_views.book_details, name='book_details'),
    path('book-details/', page_views.book_details, name='book_details_no_id'),
    path('profile/', page_views.profile, name='profile'),
    path('manage-books/', page_views.manage_books, name='manage_books'),
    path('add-book/', page_views.add_book, name='add_book'),
    path('edit-book/<int:book_id>/', page_views.edit_book, name='edit_book'),
    path('edit-book/', page_views.edit_book, name='edit_book_no_id'),
    path('manage-users/', page_views.manage_users, name='manage_users'),
    path('search/', page_views.search, name='search'),
    path('forgot-password/', page_views.forgot_password, name='forgot_password'),
    path('reset-password/<str:uidb64>/<str:token>/', page_views.reset_password, name='reset_password_page'),
]
