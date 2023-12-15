
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="homepage"),
    path('register/',views.register,name="register"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('profile/',views.profile,name="profile"),
    path('pass_change/',views.pass_change,name="pass_change"),
    path('pass_change2/',views.pass_change2,name="pass_change2"),
]
