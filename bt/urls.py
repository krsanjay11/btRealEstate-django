
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="Home"),
    path('about/',views.about,name="about"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('listing/',views.listing,name="listing"),
    path('listings/',views.listings,name="listings"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('search/',views.search,name="search"),
]
