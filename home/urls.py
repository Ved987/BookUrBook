from django.urls import path 
from . import views

urlpatterns = [path('',views.home_view, name='Index page'), 
               path('home/', views.home_view, name= 'home'),
               path('Browse/',views.browse_view,name='Browse'),
            ]