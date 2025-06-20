from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('home/', views.home),
    path('about/', views.about),
    path('login/',views.user_login, name='login'),
    path('signup/',views.signup, name='signup'),
    path('addrecipe/',views.addrecipe, name='addrecipe'),
    path('feedback/',views.feedback),
    path('recipes/', views.recipes, name='recipes'),
    path('footer/', views.footer, name='footer'),
    # path('header/', views.header, name='header'),
    # path('navbar/', views.navbar, name='navbar'),
    # path('search/', views.search, name='search'),
    # path('contact/', views.contact, name='contact'),
    # path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
    # path('recipe/<int:id>/edit/', views.edit_recipe, name='edit_recipe'),
    # path('recipe/<int:id>/delete/', views.delete_recipe, name='delete_recipe'),
    # path('recipe/<int:id>/like/', views.like_recipe, name='like_recipe'),
    # path('recipe/<int:id>/comment/', views.comment_recipe, name='comment_recipe'),
    # path('recipe/<int:id>/comment/delete/', views.delete_comment, name='delete_comment'),
]