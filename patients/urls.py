from django.urls import path
from . import views

urlpatterns = [
    path('',views.userLogin,name='login'),
    path('logout/',views.userLogout,name="logout"),
    path('home/',views.home, name="home"),
    path('about/', views.about,name="about"),
    path('register/', views.register,name="register"),
     path('register/<int:id>/', views.register,name="update"),
    path('delete/<int:id>/', views.delete,name="delete"),
]