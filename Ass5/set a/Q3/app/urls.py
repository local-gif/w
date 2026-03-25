from django.urls import path
from . import views
urlpatterns=[
path('',views.home,name='home'),
path('second/',views.second,name='second'),
path('redirect/',views.redirect_page,name='redirect'),
]