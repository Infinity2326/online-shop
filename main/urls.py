from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from onlineshop import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login', views.login),
    path('register',views.register)
]