from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about,name='about'),
    path('ice', views.ice, name='ice'),
    path('flash',views.flash, name='flash'),
    path('login', views.login, name='login'),


]
