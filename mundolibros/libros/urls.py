from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    
    path('authors/', views.author_list, name='author_list'),
    path('author/create/', views.author_create, name='author_create'),
    path('author/<int:pk>/update/', views.author_update, name='author_update'),
    path('author/<int:pk>/delete/', views.author_delete, name='author_delete'),
    
    path('books/', views.book_list, name='book_list'),
    path('book/create/', views.book_create, name='book_create'),
    path('book/<int:pk>/update/', views.book_update, name='book_update'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
    
    path('reviews/', views.review_list, name='review_list'),
    path('review/create/', views.review_create, name='review_create'),
    path('review/<int:pk>/update/', views.review_update, name='review_update'),
    path('review/<int:pk>/delete/', views.review_delete, name='review_delete'),
    
    path('search/', views.search, name='search'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    
    path('authors/', views.author_list, name='author_list'),
    path('author/create/', views.author_create, name='author_create'),
    path('author/<int:pk>/update/', views.author_update, name='author_update'),
    path('author/<int:pk>/delete/', views.author_delete, name='author_delete'),
    
    path('books/', views.book_list, name='book_list'),
    path('book/create/', views.book_create, name='book_create'),
    path('book/<int:pk>/update/', views.book_update, name='book_update'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
    
    path('reviews/', views.review_list, name='review_list'),
    path('review/create/', views.review_create, name='review_create'),
    path('review/<int:pk>/update/', views.review_update, name='review_update'),
    path('review/<int:pk>/delete/', views.review_delete, name='review_delete'),
    
    path('search/', views.search, name='search'),
]
 
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    
    path('authors/', views.author_list, name='author_list'),
    path('author/create/', views.author_create, name='author_create'),
    path('author/<int:pk>/update/', views.author_update, name='author_update'),
    path('author/<int:pk>/delete/', views.author_delete, name='author_delete'),
    
    path('books/', views.book_list, name='book_list'),
    path('book/create/', views.book_create, name='book_create'),
    path('book/<int:pk>/update/', views.book_update, name='book_update'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
    
    path('reviews/', views.review_list, name='review_list'),
    path('review/create/', views.review_create, name='review_create'),
    path('review/<int:pk>/update/', views.review_update, name='review_update'),
    path('review/<int:pk>/delete/', views.review_delete, name='review_delete'),
    
    path('search/', views.search, name='search'),
]
path('about/', views.about, name='about'),
