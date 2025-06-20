from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index),
    path('home/', views.home),
    path('about/', views.about),
    path('login/',views.login),
    path('signup/',views.signup),
    path('addrecipe/',views.addrecipe),
    path('feedback/',views.feedback),
    path('recipes/', views.recipes, name='recipes')
]